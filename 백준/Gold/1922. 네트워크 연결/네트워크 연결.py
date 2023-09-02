import sys

def find(parent, x):
    # 루트노드가 아닐경우
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

input = sys.stdin.readline

n = int(input())
m = int(input())

# root node
parent = [i for i in range(n+1)]

# edge
edges = []

for i in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# edge sort
edges.sort()

res = 0

for cost, a, b in edges:
    nodeA = find(parent, a)
    nodeB = find(parent, b)
    # 루트노드가 다를 경우
    if nodeA != nodeB:
        union(parent, nodeA, nodeB)
        res += cost

print(res)