import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())

q = deque([i for i in range(1, N+1)])
q_1 = deque([])
cnt = 0
while q:
    cnt += 1
    if(cnt % M == 0):
        q_1.append(q.popleft())
    else:
        q.append(q.popleft())


print("<" + ", ".join(map(str, q_1)) + ">")