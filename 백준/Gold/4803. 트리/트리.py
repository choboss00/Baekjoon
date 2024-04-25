idx = 1

def dfs(start_node):
    # cycle 발생 여부 체크
    cycle_check = False
    stack = [start_node]
    cycle = set()

    visited[start_node] = True
    cycle.add(start_node)

    while stack:
        #print("dfs 진행중 : ", stack)
        #print("현재 사이클 : ", cycle)
        now_node = stack.pop()

        # 사이클이 있는 경우
        if len(cycle & set(trees[now_node])) > 1:
            #print(f"사이클 발생 [ cycle : {cycle} , tree : {trees[now_node]} ]")
            cycle_check = True

        for i in trees[now_node]:
            if not visited[i]:
                cycle.add(i)
                stack.append(i)
                visited[i] = True

    return cycle_check

while True:
    n, m = map(int, input().split())
    # 종료 조건
    if n == 0 and m == 0:
        break

    trees = {i:[] for i in range(1, n+1)}

    #print("현재 트리 : ", trees)

    for _ in range(m):
        a, b = map(int, input().split())
        # 각 원소 연결하기
        trees[a].append(b)
        trees[b].append(a)

    #print("그래프 연결 후 트리 : ", trees)
    ans = 0

    visited = [False for _ in range(n+1)]

    for i in range(1, n+1):
        if not visited[i]:
            if not dfs(i):
                ans += 1

    if ans == 0:
        print(f"Case {idx}: No trees.")
    elif ans == 1:
        print(f"Case {idx}: There is one tree.")
    else:
        print(f"Case {idx}: A forest of {ans} trees.")

    # index 증가
    idx += 1

