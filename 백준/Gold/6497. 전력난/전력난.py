import sys

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

input = sys.stdin.readline

while True:
    m, n = map(int, input().split())

    if n == 0 and m == 0:
        break

    # root node
    parent = [i for i in range(m+1)]

    # edge
    edges = []

    total_cost = 0

    for i in range(n):
        x, y, z = map(int, input().split())

        edges.append((z, x, y))
        total_cost += z

    edges.sort()

    res = 0

    for cost, a, b in edges:
        nodeA = find(parent, a)
        nodeB = find(parent, b)

        if nodeA != nodeB:
            union(parent, nodeA, nodeB)
            res += cost

    print(total_cost - res)