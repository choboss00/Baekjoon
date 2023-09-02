import sys
def find(parent, x):
    # 루트노드 찾기
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

input = sys.stdin.readline
# 행성의 개수
n = int(input())
# node
parent = [i for i in range(n+1)]
# x, y, z
x, y, z = [], [], []

for i in range(1,n+1):
    a, b, c = map(int, input().split())
    x.append((a, i))
    y.append((b, i))
    z.append((c, i))

# 좌표 정렬
x.sort()
y.sort()
z.sort()

edges = []

for i in range(n-1):
    abs_x = x[i+1][0] - x[i][0]
    abs_y = y[i+1][0] - y[i][0]
    abs_z = z[i+1][0] - z[i][0]
    # x, y, z 넣어주기
    edges.append((abs_x, x[i][1], x[i+1][1]))
    edges.append((abs_y, y[i][1], y[i + 1][1]))
    edges.append((abs_z, z[i][1], z[i + 1][1]))

# 최소 비용으로 정렬하기
edges.sort()

# 비용
ans = 0

# 간선 정보를 확인하며 크루스칼 알고리즘 수행
for cost, a, b in edges:
    # 루트 노드 찾기
    nodeA = find(parent, a)
    nodeB = find(parent, b)

    # find 연산 -> union 연산
    if nodeA != nodeB:
        union(parent, nodeA, nodeB)
        ans += cost

print(ans)