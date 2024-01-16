"""
## 녹색 옷 입은 애가 젤다지?

## 문제
1. 링크의 위치 : N * N 크기의 동굴 제일 왼쪽에 위치 (0, 0)

2. 링크는 동굴의 반대편 출구, 제일 오른쪽 아래 칸인 (N-1, N-1) 까지 이동해야 함

3. 동굴의 각 칸마다 도둑루피가 잇음
- 이 칸을 지나면 해당 도둑루피의 크기만큼 소지금을 잃게 됨

4. 링크는 잃는 금액을 최소로 하여 동굴 건너편까지 이동해야 하며, 한 번에 상하좌우 인접한 곳으로 1칸씩 이동 가능

5. 링크가 잃을 수 밖에 없는 최소 금액 구하기

## 입력
1. 여러 개의 테스트 케이스

2. 동굴의 크기를 나타내는 정수 N

3. N = 0 일 경우 종료

4. 동굴의 각 칸에 있는 도둑루피의 크기가 공백으로 구분되어 차례대로 주어짐

## 출력
1. 형식에 맞춰 출력하기

## 풀이
1. 다익스트라
- 출발 노드 설정
- 최단 거리 테이블 초기화
- 방문하지 않은 노드 중, 최단 거리가 가장 짧으 노드 선택
- 해당 노드를 거쳐 다른 노드 비용 계산, 최단 거리 테이블 갱신
"""
import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline

cnt = 1

while True:
    N = int(input())

    if N == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(N)]
    distance = [[INF] * N for _ in range(N)]

    queue = []

    heapq.heappush(queue, (graph[0][0], 0, 0)) # 초기 좌표

    while queue:
        dist, x, y = heapq.heappop(queue)

        for dx, dy in ((-1,0),(1,0),(0,-1),(0,1)):
            nx = x + dx
            ny = y + dy

            if 0 <= nx < N and 0 <= ny < N:
                if dist + graph[ny][nx] < distance[ny][nx]: # 기존 값과 비교
                    # 초기화
                    distance[ny][nx] = dist + graph[ny][nx]
                    heapq.heappush(queue, (distance[ny][nx], nx, ny))

    print(f"Problem {cnt}: {distance[-1][-1]}")
    cnt += 1




