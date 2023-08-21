import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int, input().split())

# 위상 정렬
graph = [[] for _ in range(n+1)]
# 진입 차수
indegree = [0] * (n+1)

for _ in range(m):
    fr, se = map(int, input().split())
    # 방향이 있는 그래프
    graph[fr].append(se)
    indegree[se] += 1

queue = deque()
res = []

for i in range(1, n+1):
    # 진입차수가 0 인 원소를 큐에 담고
    if indegree[i] == 0:
        queue.append(i)
# 큐의 원소를 빼고
while queue:
    cur = queue.popleft()
    # 출력할 리스트에 담고 ( 이미 사용한 원소니 )
    res.append(cur)

    for i in graph[cur]:
        indegree[i] -= 1

        if indegree[i] == 0:
            queue.append(i)

print(*res)