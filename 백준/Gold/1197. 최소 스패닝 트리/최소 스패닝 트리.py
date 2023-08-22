import sys

def find(parent, x):
    # 루트를 찾았을 경우 ( 원소값이 자기 자신 )
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)

    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB

input = sys.stdin.readline

v, e = map(int, input().split())
# 노드의 갯수
parent = [0] * (v+1)

edges = []
res = 0
# 노드 설정
for i in range(1, v+1):
    parent[i] = i

# 간선 정보 입력받기
for _ in range(e):
    a, b, cost = map(int, input().split())

    edges.append((cost, a, b))
# 가중치 기준 정렬
edges.sort()

for edge in edges:
    cost, a, b = edge

    # 사이클이 발생하지 않을 경우 최소 스패닝 트리에 포함
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        res += cost

print(res)