"""
## 16924번 : 십자가 찾기

## 문제
1. 십자가 : 가운데 *, 상하좌우 모두 같은 길이의 * 가 있는 모양

2. 크기가 N * M
- . , * 로 이루어진 격자판이 주어짐

3. 십자가만을 이용해서 격자판과 같은 모양을 만들 수 있는지 구하기
- 십자가는 서로 겹쳐도 됨
- 사용할 수 있는 십자가의 갯수 <= N * M

4. 격자판의 행, 열은 1번부터 시작

## 입력
1. 격자판의 크기 N, M

## 출력
1. 십자가만 이용해서 입력으로 주어진 격자판을 만들 수 없는 경우
- -1 출력

2. 만들 수 있는 경우 필요한 십자가의 수 k 출력하기

## 풀이
1. * 를 중심으로 상하좌우 체크
- * 가 다 있을 경우 -> 십자가 + 1, 위치 좌표 저장, 한칸 더 이동
- * 의 갯수에서 십자가의 * 갯수만큼 차감

2. 만약 * 의 갯수가 양수 -> -1 출력
- 그렇지 않으면 십자가의 갯수와 위치 정보 출력
"""
import sys
import copy

input = sys.stdin.readline

n, m = map(int, input().split())

# board
board = [list(input().strip()) for _ in range(n)]

십자가 = 0
십자가_좌표 = []

d = [(0,1), (0,-1), (1,0), (-1,0)]

copy_board = copy.deepcopy(board)

for y in range(n):
    for x in range(m):
        if board[y][x] == '*':
            위 = 아래 = y
            왼쪽 = 오른쪽 = x
            십자가_크기 = 0
            while True:
                위 += 1
                아래 -= 1
                왼쪽 -= 1
                오른쪽 += 1
                if 0 <= 위 < n and 0 <= 아래 < n and 0 <= 왼쪽 < m and 0 <= 오른쪽 < m and board[위][x] == '*' and board[아래][x] == '*' and board[y][왼쪽] == '*' and board[y][오른쪽] == '*':
                        십자가 += 1
                        십자가_크기 += 1
                        copy_board[위][x] = copy_board[아래][x] = copy_board[y][왼쪽] = copy_board[y][오른쪽] = '.'
                        십자가_좌표.append((y+1, x+1, 십자가_크기))
                else:
                    if 십자가_크기 > 0:
                        copy_board[y][x] = '.'
                    break
                    
for b in copy_board:
    if '*' in b:
        print(-1)
        exit(0)

print(십자가)
십자가_좌표.sort(key=lambda x:(x[0], x[1], -x[2]))
for 좌표 in 십자가_좌표:
    print(*좌표)

