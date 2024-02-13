"""
## 뱀과 사다리 게임

## 문제
1. 주사위 : 1 ~ 6

2. 게임의 크기 : 10 * 10
- 보드판에는 1부터 100까지 수가 하나씩 순서대로 적혀져 있음

3. 플레이어는 주사위를 굴려서 나온 수 만큼 이동해야 함
- 만약 주사위를 굴린 결과가 100번 칸을 넘어간다면 이동할 수 없음

4. 도착한 칸이 사다리면, 사다리를 타고 위로 올라감

5. 뱀이 있는 칸에 도착하면, 뱀을 따라서 내려가게 됨

6. 목표 : 1번 칸에서 100번 칸에 도착하는 것

7. 게임판의 상태가 주어졌을 때, 100번 칸에 도착하기 위해 주사위를 굴려야 하는 횟수의 최솟값 구하기

## 입력
1. 게임판에 있는 사다리의 수 N, 뱀의 수 M

2. 둘째줄 부터 N개의 줄에는 사다리의 정보를 의미하는 x, y : x 번 칸에 도착하면, y번 칸으로 이동한다는 의미

3. 다음 M 개의 줄에는 뱀의 정보를 의미하는 u, v : u번 칸에 도착하면, v번 칸으로 이동한다는 의미

4. 1번 칸과 100번 칸은 뱀과 사다리의 시작 또는 끝이 아님

5. 모든 칸은 최대 하나의 사다리 또는 뱀을 가지고 있으며, 동시에 두 가지를 모두 가지고 있는 경우는 없음

6. 항상 100번 칸에 도착할 수 있는 입력만 주어짐

## 출력
1. 100번 칸에 도착하기 위해 주사위를 최소 몇 번 굴려야 하는지 출력하기

## 풀이
1. BFS 탐색 진행

2. 각 위치별로 뱀인지, 사다리인지, 일반 칸인지 구분할 수 있어야 함

3. 뱀과 사다리 값을 딕셔너리로 관리하면 더 편할 듯 함

"""
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

visited = [False for _ in range(101)]
ladders = {}
snakes = {}

for _ in range(n):
    a, b = map(int, input().split())
    if a not in ladders:
        ladders[a] = b

for _ in range(m):
    a, b = map(int, input().split())
    if a not in snakes:
        snakes[a] = b

queue = deque()
# 첫 위치 담기
queue.append([1,0])

while queue:
    x, cnt = queue.popleft()

    visited[x] = True

    for i in range(1, 7):
        nx = x + i

        # 예외 처리
        if nx < 0 or nx > 100:
            continue

        if nx == 100:
            print(cnt + 1)
            exit(0)

        if nx in ladders and not visited[nx]:
            visited[nx] = True
            visited[ladders[nx]] = True
            queue.append([ladders[nx], cnt+1])
        if nx in snakes and not visited[nx]:
            visited[nx] = True
            visited[snakes[nx]] = True
            queue.append([snakes[nx], cnt+1])
        if not visited[nx]:
            visited[nx] = True
            queue.append([nx, cnt+1])
