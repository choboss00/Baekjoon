"""
## 특정한 최단 경로

## 문제
1. 방향성이 없는 그래프

2. 1번 정점에서 N번 정점으로 최단 거리를 이동하려고 함

3. 2가지 조건을 만족하면서 이동하는 특정한 최단 경로를 구하고자 함
- 임의로 주어진 두정점은 반드시 통과해야 함
- 한번 이동했던 정점은 물론, 한번 이동했던 간선도 다시 이동할 수 있음

4. 1번 정점에서 N번 정점으로 이동할 대, 주어진 두 정점을 반드시 거치면서 최단 경로로 이동하는 프로그램 작성하기

## 입력
1. 정점의 개수 N, 간선의 개수 E

2. 3개의 정수 a, b, c
- a번 정점에서 b번 정점까지 양방향의 길
- 그 거리는 c

3. 반드시 거쳐야 하는 두 개의 서로 다른 정점 번호 v1, v2

4. 임의의 두 정점 u 와 v 사이에는 간선이 최대 1개 존재함

## 출력
1. 두 개의 정점을 지나는 최단 경로의 길이를 출력하기

2. 그런 경로가 없을 때, -1 출력

"""
import sys
import heapq

INF = 1e8

input = sys.stdin.readline

n, e = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

# 반드시 지나야하는 정점
v1, v2 = map(int, input().split())

def dijkstra(start_node):
    queue = []

    heapq.heappush(queue, [0, start_node])
    # 거리
    distances = [INF] * (n + 1)
    distances[start_node] = 0

    while queue:
        current_dist, current_node = heapq.heappop(queue)

        if distances[current_node] < current_dist:
            continue

        for i in graph[current_node]:
            if i[1] + current_dist < distances[i[0]]:
                distances[i[0]] = current_dist + i[1]
                heapq.heappush(queue, [current_dist + i[1], i[0]])

    return distances

path1 = dijkstra(1)
path2 = dijkstra(v1)
path3 = dijkstra(v2)

v1_path = path1[v1] + path2[v2] + path3[n]
v2_path = path1[v2] + path3[v1] + path2[n]

ans = min(v1_path, v2_path)

print(ans if ans < INF else -1)