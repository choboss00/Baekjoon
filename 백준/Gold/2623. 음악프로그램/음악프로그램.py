import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

# 위상 정렬
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for _ in range(m):
    # 덱으로 입력받기
    lst = deque(map(int, input().split()))
    # 반복
    k = lst.popleft()

    for i in range(k-1):
        graph[lst[i]].append(lst[i+1])
        indegree[lst[i+1]] += 1

queue = deque()
res = []
for i in range(1, n+1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    cur = queue.popleft()
    res.append(cur)

    for v in graph[cur]:
        indegree[v] -= 1

        if indegree[v] == 0:
            queue.append(v)

if len(res) != n:
    print(0)
else:
    for ans in res:
        print(ans)