"""
## 택배 배송

## 문제
1. 최소한의 소들을 만나면서 택배를 배달하고 싶음

2. 지도, N 개의 헛간, M 개의 양방향 길, 각각의 길은 C_i 마리의 소가 있음

3. 소들의 길은 두 개의 떨어진 헛간인 A_i 와 B_i 를 이음
- 두개의 헛간은 하나 이상의 길로 연결되어 있을 수도 있음

4. 농부 현서는 헛간 1에 있고 농부 찬홍이는 헛간 N 에 있음

5. 농부 현서의 지도가 주어지고, 지나가는 길에 소를 만나면 줘야할 여물의 비용이 주어질 때 최소 여물 구하기

## 입력
1. N, M

2. 3개의 정수 A_i, B_i, C_i ( A -> B, 비용 C )

## 출력
1. 최소 여물 출력하기

## 풀이
1. 다익스트라

"""
import sys
import heapq

INF = 1e8

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

start, end = 1, n
distance = [INF] * (n+1)

def dijkstra(start_node):
    queue = []

    heapq.heappush(queue, ((0, start_node)))
    distance[start_node] = 0

    while queue:
        dist, now = heapq.heappop(queue)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            if dist + i[1] < distance[i[0]]: # 현재 길이보다 경유해서 가는게 더 저렴할 경우
                distance[i[0]] = dist + i[1]
                heapq.heappush(queue, (dist + i[1], i[0]))

dijkstra(start)

print(distance[end])