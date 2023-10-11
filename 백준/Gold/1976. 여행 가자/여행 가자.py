import sys

def find(node):
    if parents[node] != node:
        parents[node] = find(parents[node])
    return parents[node]

def union(nodeA, nodeB):
    nodeA = find(nodeA)
    nodeB = find(nodeB)

    if nodeA < nodeB:
        parents[nodeB] = nodeA
    else:
        parents[nodeA] = nodeB

input = sys.stdin.readline

# 도시의 수
n = int(input())
# 여행 계획에 속한 도시들의 수
m = int(input())
# node
parents = [i for i in range(n+1)]

for i in range(1, n+1):
    links = list(map(int, input().split()))

    cnt = i

    for j in range(1, n+1):
        if links[j-1] == 0: # 연결 X
            continue
        else: # 연결 O
            union(cnt, j)


checkLinks = list(map(int, input().split()))

ans_set = set()

for link in checkLinks:
    ans_set.add(find(link))

if len(ans_set) == 1:
    print('YES')
else:
    print('NO')