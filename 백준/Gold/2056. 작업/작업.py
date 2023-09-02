import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
cost = [0] * (n+1)

for i in range(1, n+1):
    # 작업
    l = list(map(int, input().split()))
    # 비용 저장
    cost[i] = l[0]

    se = l[1]
    # 선행 작업이 있을 경우
    if se != 0:
        for j in range(2, se+2):
            graph[l[j]].append(i)
            indegree[i] += 1

queue = deque()
dp = [0] * (n+1)

for i in range(1, n+1):
    if indegree[i] == 0:
        queue.append(i)
        dp[i] = cost[i]

while queue:
    cur = queue.popleft()

    cost_list = []

    for i in graph[cur]:
        indegree[i] -= 1
        dp[i] = max(dp[cur] + cost[i], dp[i])

        if indegree[i] == 0:
            queue.append(i)

print(max(dp))