import heapq

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())

    graph[a].append([b,c])
    graph[b].append([a,c])

#print("현재 그래프 : ", graph)

ans_set = set()

# 현재 비용
distance = [10000001 for _ in range(N+1)]

#print("현재 비용 : ", distance)
ans_dict = {i:[0, 100000001] for i in range(N+1)}

#print("현재 딕셔너리 : ", ans_dict)
def dijkstra(start_node):
    queue = []
    # 현재 힙에 [시작 노드, 초기 비용] 넣기
    heapq.heappush(queue, [start_node, 0])

    # 현재 거리 초기화
    distance[start_node] = 0

    while queue:
        now_node1, now_distance = heapq.heappop(queue)

        if distance[now_node1] < now_distance:
            continue

        # 연결된 노드 탐색
        for i in graph[now_node1]:
            # 현재 노드에서 연결된 노드 탐색
            next_node, next_distance = i[0], i[1]

            if distance[now_node1] + next_distance < distance[next_node]:
                distance[next_node] = distance[now_node1] + next_distance
                queue.append([next_node, distance[next_node]])

                if distance[next_node] < ans_dict[next_node][1]:
                    ans_dict[next_node] = [now_node1, distance[next_node]]

dijkstra(1)

#print("다익스트라 탐색 후 : ", distance)

#print("다익스트라 탐색 후 딕셔너리 : ", ans_dict)

print(len(ans_dict)-2)

for k, v in ans_dict.items():
    if k == 0 or k == 1:
        continue
    print(k, v[0])