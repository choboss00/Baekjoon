import sys

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    parent[max(a,b)] = min(a,b)

input = sys.stdin.readline

n, m = map(int, input().split())

# parent
parent = [i for i in range(n+1)]

edges = []

xy_list = []

for i in range(n):
    xy_list.append(list(map(int, input().split())))
for _ in range(m):
    a1, b1 = map(int, input().split())

    node1 = find(parent, a1)
    node2 = find(parent, b1)

    union(parent, node1, node2) # 미리 이어주기

for i in range(n):
    x1, y1 = xy_list[i]
    for j in range(i+1, n):
        x2, y2 = xy_list[j]

        cost = pow((x2-x1) ** 2 + (y2-y1) ** 2, 0.5)

        edges.append((cost, i+1, j+1))

# cost 기준으로 정렬
edges.sort()

res = 0

for cost, a, b in edges:
    nodeA = find(parent, a)
    nodeB = find(parent, b)

    if nodeA != nodeB:
       union(parent, nodeA, nodeB)
       res += cost

print('%.2f' % (res) )