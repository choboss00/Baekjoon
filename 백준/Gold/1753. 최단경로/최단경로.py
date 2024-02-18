"""
## 최단경로

## 문제
1. 방향 그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램 작성하기

## 입력
1. 정점의 개수 V와 간선의 개수 E
- 모든 정점에는 1부터 V까지 번호가 매겨져 있다고 가정

2. 둘째 줄 : 시작정점의 번호 K

3. 셋째 줄 ~ E개의 줄에 걸쳐 각 간선을 나타내는 세 개의 정수 ( u, v, w ) 가 순서대로 주어짐
- u 에서 v 로 가는 가중치 w 인 간선이 존재

4. u 와 v 는 서로 다르며, w 는 10 이하의 자연수
- 서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음

## 출력
1. 첫째 줄 부터 V 개의 줄에 걸쳐, i번재 줄에 i번 정점으로의 최단 경로의 경로값 출력하기
- 시작점 자신은 0 으로 출력
- 경로가 존재하지 않는 경우, INF 출력

## 풀이
1. 다익스트라

"""
import sys
import heapq

INF = 1e8

input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())

graph = [[] for _ in range(v+1)]
distance = [INF] * (v+1)

for _ in range(e):
    # 부모, 자식, 비용
    p, c, cost = map(int, input().split())

    graph[p].append([c, cost])

def dijkstra(start_node):
    queue = []
    # heapq 에 push
    heapq.heappush(queue, (0, start_node))
    # 방문 처리
    distance[start_node] = 0

    while queue:
        dist, now = heapq.heappop(queue)
        # 이미 입력된 값이 현재 노드까지의 거리보다 작을 경우
        if distance[now] < dist:
            continue

        for i in graph[now]:
            if dist + i[1] < distance[i[0]]: # 기존 입력 값보다 작은 값이 나올 경우
                # 거리 조정
                distance[i[0]] = dist + i[1]
                heapq.heappush(queue, (dist + i[1], i[0]))

dijkstra(k)

for i in range(1,v+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])
