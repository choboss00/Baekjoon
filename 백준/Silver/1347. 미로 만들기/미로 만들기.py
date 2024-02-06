"""
## 미로 만들기

## 문제
1. 현 위치 : 미로 안의 한 칸에 남쪽을 보며 서있음

2. 미로 : 직사각형 격자 모양
- 이동할 수 있는 칸, 벽

3. 모든 행과 열에는 적어도 하나의 이동할 수 있는 칸이 있음

4. 미로의 지도를 자기 노트만을 이용해서 그리려고 함

5. F : 앞으로 한 칸 이동, L : 왼쪽, R : 오른쪽 방향 전환

## 입력
1. 노트에 적은 내용의 길이

## 출력
1. 미로 지도 출력하기
- '.' : 이동할 수 있는 칸
- '#' : 벽

## 풀이
1. 현 위치 : 남쪽을 바라보고 있음

2. 자신이 걸어간 칸을 제외한 나머지 부분은 전부 벽이라고 봐도 무방함
"""
import sys

input = sys.stdin.readline

n = int(input())
paper = list(input().strip())

visited = [[-1 for _ in range(2 * n + 1)] for _ in range(2 * n + 1)]

# 현 위치 방문 처리, 방향 : 남쪽
# 0 : 남, 1 : 서, 2 : 북, 3 : 동
x, y, d = n, n, 0
visited[y][x] = '.' # . 인 경우 빈 공간, # 인 경우 벽이라고 가정

for p in paper:
    if p == 'R':
        d = (d + 1) % 4
    elif p == 'L':
        d = (d - 1) % 4
    else: # 앞으로 이동
        # 남쪽으로 이동하는 경우
        if d == 0:
            y += 1
            visited[y][x] = '.'
        # 서쪽으로 이동하는 경우
        elif d == 1:
            x -= 1
            visited[y][x] = '.'
        elif d == 2:
            y -= 1
            visited[y][x] = '.'
        elif d == 3:
            x += 1
            visited[y][x] = '.'

# 양 끝값을 기록하는 변수
_maxX, _maxY, _minX, _minY = -1, -1, 111, 111

for i in range(len(visited)):
    if '.' not in visited[i]:
        continue
    # 가장 윗 부분 위치 구하기
    if _minY >= i:
        _minY = i
    # 가장 아랫 부분 위치 구하기
    if _maxY < i:
        _maxY = i
    for j in range(len(visited[i])):
        if visited[i][j] == '.':
            if _minX >= j:
                _minX = j
            if _maxX < j:
                _maxX = j

for y in visited[_minY:_maxY+1]:
    for x in y[_minX:_maxX+1]:
        if x == '.':
            print(x, end='')
        else:
            print("#", end='')
    print()
