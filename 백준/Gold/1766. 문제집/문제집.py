import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())

# 위상 정렬
queue = []
indegree = [0] * (n+1)
# 마지막에 출력해야할 리스트
res = []
# 그래프
graph = [[] for _ in range(n+1)]

for _ in range(m):
    # a 를 b 보다 먼저 풀어야 함
    a,b = map(int, input().split())
    # 그래프에 넣기
    graph[a].append(b)
    # 진입차수 설정
    indegree[b] += 1
# 진입차수가 0 인 노드들을 큐에 넣기
for i in range(1, n+1):
    if indegree[i] == 0:
        heapq.heappush(queue, i)


while queue:
    cur = heapq.heappop(queue)
    res.append(cur)

    for v in graph[cur]:
        indegree[v] -= 1

        if indegree[v] == 0:
            heapq.heappush(queue, v)

print(*res)