import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

T = int(input())

def dfs(x):
    global ans
    # 방문 처리
    visited[x] = True
    team_list.append(x)
    next_node = parents[x]
    # 다음 노드를 방문하지 않은 경우
    if not visited[next_node]:
        dfs(next_node)
    else:
        if next_node in team_list:
            ans += len(team_list[team_list.index(next_node):])

for _ in range(T):
    # 학생의 수
    n = int(input())
    ans = 0

    # 선택된 학생들의 번호가 주어짐 ( 부모 )
    parents = [0] + list(map(int, input().split()))

    # 방문 처리
    visited = [False for _ in range(n+1)]

    for i in range(1, n+1):
        if not visited[i]:
            team_list = []
            dfs(i)
    print(n-ans)
