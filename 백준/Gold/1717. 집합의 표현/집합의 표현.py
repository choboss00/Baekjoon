import sys

sys.setrecursionlimit(10**5)
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(node1, node2):
    if node1 < node2:
        parent[node2] = node1
    else:
        parent[node1] = node2

input = sys.stdin.readline

n, m = map(int, input().split())

# parent
parent = [i for i in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    # b, c 의 부모 찾기
    b = find(b)
    c = find(c)

    # a == 0 일 때, 합하기
    if a == 0:
        union(b, c)
    else:
        if b == c:
            print('YES')
        else:
            print('NO')