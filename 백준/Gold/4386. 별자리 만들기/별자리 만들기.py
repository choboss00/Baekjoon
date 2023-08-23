import sys

def find(parent, x):
    # 루트노드 일 경우
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, nodeA, nodeB):
    if nodeA < nodeB:
        parent[nodeB] = nodeA
    else:
        parent[nodeA] = nodeB


input = sys.stdin.readline

n = int(input())
xy_list = []

for _ in range(n):
    x, y = map(float, input().split())

    xy_list.append((x,y))

# 그래프
parent = [i for i in range(n+1)]

# 거리의 비용을 저장하는 리스트
di_list = []
# 마지막은 안해도 됨
for i in range(n-1):
    x1, y1 = xy_list[i]
    for j in range(i+1, n):
        x2, y2 = xy_list[j]

        cost = pow((x2 - x1) ** 2 + (y2 - y1) ** 2, 0.5)
        di_list.append((cost, i, j))
# 정렬
di_list.sort()
res = 0
for edge in di_list:
    cost, a, b = edge

    nodeA = find(parent, a)
    nodeB = find(parent, b)

    if nodeA != nodeB:
        union(parent, nodeA, nodeB)
        res += cost

print(round(res, 2))