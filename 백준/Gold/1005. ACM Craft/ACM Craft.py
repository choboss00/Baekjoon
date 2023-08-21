import sys
from collections import deque

input = sys.stdin.readline
# testCase
t = int(input())

for _ in range(t):
    # 건물의 개수 n, 건설순서 규칙의 총 갯수 k
    n, k = map(int, input().split())

    # 위상정렬 그래프
    graph = [[] for _ in range(n)]
    indegree = [0] * n

    # 각 건물당 걸리는 시간
    n_time = list(map(int, input().split()))
    # 건설순서 x, y
    for _ in range(k):
        x,y = map(int, input().split())
        # index 맞추기
        x -= 1
        y -= 1
        # 위상정렬 설정
        graph[x].append(y)
        indegree[y] += 1
    # 찾아야할 원소
    la = int(input())
    la -= 1

    queue = deque()
    res = [0 for _ in range(n)]

    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)
            res[i] = n_time[i]

    while queue:
        cur = queue.popleft()

        for v in graph[cur]:
            indegree[v] -= 1
            res[v] = max(res[cur]+n_time[v], res[v])

            if indegree[v] == 0:
                queue.append(v)

    print(res[la])