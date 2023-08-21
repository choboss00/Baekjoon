import sys
sys.setrecursionlimit(100_000)
def dfs(node):
    # 방문한 경우
    if visited[node]:
        return

    # 현 위치 방문 표시
    visited[node] = True
    # 다음 노드 탐색하기
    for v in graph[node]:
        dfs(v)
    res.append(str(node))

input = sys.stdin.readline

n,m = map(int, input().split())

# dfs
graph = [[] for _ in range(n+1)]

for _ in range(m):
    fr, se = map(int, input().split())
    # 방향이 있는 그래프
    graph[se].append(fr)

res = []
visited = [False] * (n+1)

for i in range(1, n+1):
    dfs(i)

print(' '.join(res))