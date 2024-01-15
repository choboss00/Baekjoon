"""
## 경로 찾기

## 문제
1. 가중치 없는 방향 그래프 G

2. 모든 정점 (i, j) 에 대해서, i 에서 j 로 가는 길이가 양수인 경로가 있는지 구하는 프로그램 작성하기

## 입력
1. 정점의 개수 N

2. 그래프의 인접 행렬

3. i번째 줄의 j번째 숫자가 1인경우, i에서 j로 가는 간선이 존재한다는 뜻

## 출력
1. N 개의 줄에 걸쳐서 문제의 정답을 인접행렬 형식으로 출력하기

## 풀이
1. 자기 자신으로 갈 수 있는 경우 : 자기 자신에서 시작했을 때, 다시 돌아올 수 있어야 함

"""
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[0 for _ in range(n)] for _ in range(n)]

def bfs(x):
    queue = deque()
    queue.append(x)

    check = [False for _ in range(n)]

    while queue:
        prev = queue.popleft()

        for i in range(n):
            if not check[i] and graph[prev][i] == 1:
                queue.append(i)
                check[i] = True
                visited[x][i] = 1

for i in range(n):
    bfs(i)

for v in visited:
    print(*v)

