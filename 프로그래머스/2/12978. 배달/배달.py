import heapq

def solution(N, road, K):
    graph = [[] for _ in range(N+1)]
    
    # 출발점에서 각 노드까지의 최단 거리를 저장하는 리스트
    distances = [float("inf")] * (N+1)
    # 처음 위치 초기화
    distances[1] = 0
    
    for a, b, cost in road:
        graph[a].append((b, cost))
        graph[b].append((a, cost))
    
    heap = []
    # 출발점 추가하기 (비용, 출발 노드)
    heapq.heappush(heap, (0, 1))
    
    while heap:
        dist, node = heapq.heappop(heap)
        
        for next_node, next_dist in graph[node]:
            cost = dist + next_dist
            if cost < distances[next_node]:
                distances[next_node] = cost
                heapq.heappush(heap, (cost, next_node))
    
    return sum(1 for dist in distances if dist <= K)
    

"""
## 문제

## 배달
1. N개의 마을로 이루어진 나라
- 각 마을에는 1부터 N까지의 번호가 각각 하나씩 부여되어 있음

2. 각 마을은 양방향으로 통행할 수 있는 도로로 연결되어 있음
- 서로 다른 마을 간에 이동할 때는 이 도로를 지나야 함
- 도로를 지날 때 걸리는 시간은 도로별로 다름

3. 현재 1번 마을에 있는 음식점에서 각 마을로 음식 배달을 하려고 함

4. 각 마을로부터 음식 주문을 받으려고 하는데, N개의 마을 중에서 K 시간 이하로 배달이 가능한 마을에서만 주문을 받으려고 함

5. 마을의 개수 N, 각 마을을 연결하는 도로의 정보 road, 음식 배달이 가능한 시간 K 가 매개변수로 주어질 때, 음식 주문을 받을 수 있는 마을의 개수를 return 하도록 solution 함수 작성하기

## 제한사항
1. N : 1 이상, 50 이하인 자연수

2. road 의 길이 : 1 이상, 2000 이하

3. road : 마을을 연결하고 있는 각 도로의 정보

4. road : 길이가 3인 배열, 순서대로 (a, b, c) 를 나타냄
- a, b : 도로가 연결하는 두 마을의 번호
- c : 도로를 지나는데 걸리는 시간
- 두 마을 a, b 를 연결하는 도로는 여러 개가 있을 수 있음
- 한 도로의 정보가 여러 번 중복해서 주어지지 않음

5. k : 음식 배달이 가능한 시간, 1 이상 500000 이하

6. 임의의 두 마을간 항상 이동 가능한 경로가 존재함

7. 1번 마을에 있는 음식점이 k 이하의 시간에 밷라이 가능한 마을 개수 return 하기

## 풀이
1. 다익스트라

"""