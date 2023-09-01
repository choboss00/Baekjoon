import sys
from collections import deque

input = sys.stdin.readline

# 수빈 : n, 동생 : k
n, k = map(int, input().split())

# 방문 위치
parent = [-1] * 100001

queue = deque()
# 수빈의 처음 위치, 시간
queue.append((n,0))

# 방문 처리
parent[n] = 0
res = [k]
while queue:
    # 현 위치
    cur, time = queue.popleft()

    if cur == k:
        print(time)
        for i in range(time):
            res.append(parent[res[-1]])
        print(*reversed(res))
        break

    for i in (cur-1, cur+1, cur * 2):
        # 예외 처리
        if 0 <= i <= 100000:
            # 방문하지 않은 위치일 경우
            if parent[i] == -1:
                queue.append((i, time+1))
                parent[i] = cur