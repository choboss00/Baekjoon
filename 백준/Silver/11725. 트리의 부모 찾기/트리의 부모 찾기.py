"""
11725번. 트리의 부모 찾기

루트 : 1
각 노드의 부모를 구하는 프로그램 작성하기

"""
import sys
sys.setrecursionlimit(10**6)
def dfs(start_node):
    for node in tree[start_node]:
        # 만약 아직 방문하지 않은 자식 노드일 경우
        if visited[node] == 0:
            # 방문표시 ( 예를 들어 1번 노드의 경우, 자식이 6, 4 이니 6번 노드와 4번 노드가 자신의 자식이라고 표시를 남김 )
            visited[node] = start_node
            dfs(node)
input = sys.stdin.readline

n = int(input())

tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int, input().split())
    # 양방향
    tree[a].append(b)
    tree[b].append(a)

# 방문 표시
visited = [0 for _ in range(n+1)]

# dfs 호출
dfs(1)

print(*visited[2:], sep="\n")