"""
## 최소비용 구하기

## 문제
1. N 개의 도시가 있음

2. 한 도시에서 출발하여 다른 도시에 도착하는 M개의 버스가 있음

3. A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 함

4. A번째 도시에서 B번째 도시까지 가는데 드는 최소비용 출력하기
- 도시의 번호는 1부터 N까지

## 입력
1. 도시의 개수 N, 버스의 개수 M

2. 버스의 정보
- 버스의 출발 도시의 번호, 도착지의 도시 번호, 버스 비용
- 버스 비용은 0보다 크거나 같고, 10만보다 작은 정수 ( 음의 가중치는 없음 )

## 출력
1. 첫째 줄에 출발 도시에서 도착 도시까지 가는데 드는 최소 비용 출력하기

## 풀이
1. 다익스트라 알고리즘

"""
import sys
import heapq

input = sys.stdin.readline

INF = 1e8

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, cost = map(int, input().split())

    graph[a].append([b, cost])

start, end = map(int, input().split())

distance = [INF] * (n+1)

def dijkstra(start_node):
    queue = []

    # 시작 노드
    heapq.heappush(queue, (0, start_node))
    distance[start_node] = 0

    while queue:
        dist, now = heapq.heappop(queue)

        # 현재 비용과 노드를 경유해서 가는 비용을 비교하기
        if distance[now] < dist:
            continue

        for i in graph[now]:
            if i[1] + dist < distance[i[0]]:
                # 거리 조정
                distance[i[0]] = i[1] + dist
                heapq.heappush(queue, (i[1] + dist, i[0]))

dijkstra(start)

print(distance[end])
