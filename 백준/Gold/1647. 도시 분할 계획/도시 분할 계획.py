import sys
def find(parent, x):
    # 자기자신일 때 ( 루트 노드일 때 )
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rootA, rootB):
    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB

input = sys.stdin.readline

n, m = map(int, input().split())
# 노드
parent = [0] * (n+1)
# 번호
for i in range(1, n+1):
    parent[i] = i
# 간선
edges = []

for _ in range(m):
    a,b,cost = map(int, input().split())

    edges.append((cost, a, b))

# 비용을 기준으로 정렬
edges.sort()

# 총 비용
ans = 0
# 마지막 비용 기억하기
lastNum = 0
# 연결 횟수 체크
cnt = 0
for edge in edges:
    cost, a, b = edge

    rootA = find(parent, a)
    rootB = find(parent, b)
    # 루트노드가 같을 경우 그래프가 사이클이 발생함
    if rootA == rootB:
        continue

    union(parent, rootA, rootB)
    ans += cost
    lastNum = cost
    cnt += 1

    if cnt == (n-1):
        break


print(ans - lastNum)