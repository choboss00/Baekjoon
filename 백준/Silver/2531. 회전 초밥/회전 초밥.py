import sys
from collections import deque
import itertools
# 입력값
input = sys.stdin.readline

n,d,k,c = map(int, input().split())

queue = deque()
# 회전초밥 갯수 입력
for i in range(n):
    queue.append(int(input()))

# 정답
ans_list = []

for i in range(n):
    # 먹은 접시
    d_set = set(itertools.islice(queue, k))

    if c not in d_set:
        ans_list.append(len(d_set)+1)
    else:
        ans_list.append(len(d_set))

    queue.rotate(-1)

print(max(ans_list))