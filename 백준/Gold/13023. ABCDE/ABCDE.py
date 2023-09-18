import sys
def dfs(start ,cnt):
    if cnt == 4:
        print(1)
        exit(0)

    visited[start] = True

    for i in graph[start]:
        # 아직 방문하지 않은 노드일 경우
        if not visited[i]:
            # 방문처리
            dfs(i, cnt + 1)
    visited[start] = False


input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a+1].append(b+1)
    graph[b+1].append(a+1)

visited = [False] * (n+1)

for i in range(1, n+1):
    dfs(i, 0)

print(0)