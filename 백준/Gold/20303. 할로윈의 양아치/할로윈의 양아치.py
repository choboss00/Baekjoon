# N : 거리에 있는 아이들 수
# M : 아이들의 친구 관계 수
# K : 울음소리가 공명하기 위한 최소 아이의 수
import sys
from collections import deque

input = sys.stdin.readline

sys.setrecursionlimit(10**6)
N, M, K = map(int, input().split())

# 아이들이 받은 사탕의 수
Ci = list(map(int, input().split()))

# 친구 관계
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

#print("친구 관계 그래프 : ", graph)

def dfs(start_node):
    stack = [start_node]
    total_candies = 0
    total_count = 0

    while stack:
        node = stack.pop()

        if not visited[node]:
            visited[node] = True

            total_candies += Ci[node - 1]
            total_count += 1

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    stack.append(neighbor)
    return  total_candies, total_count

child_groups = []
# 방문 처리
visited = [False for _ in range(N + 1)]

for idx in range(1, N+1):
    if not visited[idx]:
        candies, count = dfs(idx)
        child_groups.append([candies, count])

child_groups.sort(key=lambda x :(-x[0], x[1]))

#print("아이들 그룹 : ", child_groups)

dp = [-float('inf')] * (K+1)
dp[0] = 0

for candies, count in child_groups:
    for j in range(K, count-1, -1):
        if dp[j-count] != -float('inf'):
            dp[j] = max(dp[j], dp[j-count] + candies)

print(max(dp[:-1]))