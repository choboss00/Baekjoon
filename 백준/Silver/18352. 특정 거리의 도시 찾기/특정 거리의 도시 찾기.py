import heapq

N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

#print("현재 그래프 출력 : ", graph)
# 각 도시간 거리
distance = [float("inf") for _ in range(N+1)]

def dijkstra(x):
    queue = []
    # heap queue 에 초기 거리 및 노드 추가
    heapq.heappush(queue, [0, x])
    # 초기 거리 초기화
    distance[x] = 0

    while queue:
        now_distance, now_node = heapq.heappop(queue)

        if distance[now_node] < now_distance:
            continue
        # 다음 노드 탐색
        for i in graph[now_node]:
            if now_distance + 1 < distance[i]:
                distance[i] = now_distance + 1
                heapq.heappush(queue, (distance[i], i))


dijkstra(X)

ans_list = []

for i in range(1, N+1):
    if i == X:
        continue
    if distance[i] == K:
        ans_list.append(i)

if len(ans_list) > 0:
    for a in ans_list:
        print(a)
else:
    print(-1)
