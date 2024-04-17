import heapq

# N : 학생 수, M : 도로, X : 모일 마을
N, M, X = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    # a 노드에 간선과 비용 추가
    graph[a].append([b, c])

# 각 학생들의 소요시간을 저장할 리스트
child_cost_list = [0 for _ in range(N+1)]

def dijkstra(start_node):
    q = []
    # 시작 노드 정보 삽입
    heapq.heappush(q, (0, start_node))

    # 시작 노드의 초기 거리 설정
    distance[start_node] = 0

    while q:
        now_distance, now_node = heapq.heappop(q)
        # 이미 비용이 작은 경우
        if distance[now_node] < now_distance:
            continue

        for next_node, next_distance in graph[now_node]:
            cost = distance[now_node] + next_distance

            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))


for i in range(1, N+1):
    distance = [int(1e9) for _ in range(N + 1)]
    # 자기자신은 탐색할 필요 없음
    if i == X:
        continue

    dijkstra(i)

    child_cost_list[i] += distance[X]

    distance = [int(1e9) for _ in range(N + 1)]

    dijkstra(X)

    child_cost_list[i] += distance[i]

print(max(child_cost_list))