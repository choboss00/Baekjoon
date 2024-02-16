"""
## 행성 연결

## 문제
1. 행성 T 에서 제국을 효과적으로 통치하기 위해 N개의 행성 간 플로우를 설치하려고 함

2. 두 행성 간 플로우를 설치하면 짧은 시간만에 이동 가능
- 치안 유지를 위해 플로우 내의 제국군을 주둔시켜야 함

3. N 개의 행성 : 1..N 으로 표시
- 행성 i 와 행성 j 사이의 플로우 관리 비용은 Cij 이며, i = j 인 경우 항상 0

4. 제국 내 모든 행성을 연결하고, 유지비용 최소화하는 프로그램 작성하기

## 입력
1. 행성의 수 N

2. 플로우 관리 비용이 N * N 행렬로 주어짐

## 출력
1. 모든 행성을 연결했을 때, 최소 플로우의 관리 비용 출력하기

## 풀이
1. union-find 이용, 최소 스패닝 트리
"""
import sys

input = sys.stdin.readline

def find(parent, x):
    if parent[x] == x: # 자기자신이 루트노드
        return x
    parent[x] = find(parent, parent[x]) # 경로 압축
    return parent[x]

def union(parent, rank, x, y):
    x = find(parent, x)
    y = find(parent, y)

    if rank[x] < rank[y]:
        parent[x] = y
    elif rank[x] > rank[y]:
        parent[y] = x
    else: # 같을 경우, 아무쪽에나 연결하고 랭크 1 올리기
        parent[x] = y
        rank[y] += 1

n = int(input())

graph = []

for i in range(n):
    n_list = list(map(int, input().split()))

    for j in range(n):
        if n_list[j] == 0: # 자기자신
            continue

        graph.append([i+1, j+1, n_list[j]])

parents = [i for i in range(n+1)]
ranks = [0 for _ in range(n+1)]
min_cost, edge = 0, 0

graph.sort(key=lambda x:x[2])

for g in graph:
    if edge == n-1: # 모든 간선이 연결된 경우
        break

    x, y = find(parents, g[0]), find(parents, g[1])
    # 루트 노드가 서로 다를경우 합치기
    if x != y:
        union(parents, ranks, x, y)
        min_cost += g[2]
        edge += 1

print(min_cost)

