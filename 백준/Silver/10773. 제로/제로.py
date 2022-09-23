import sys
from collections import deque

# 정수 K
K = int(sys.stdin.readline().strip())

# 정수 받기
queue = deque([])
for i in range(K):
    num = int(sys.stdin.readline().strip())
    if(num != 0):
        queue.append(num)
    else:
        queue.pop()

# 합 구하기
sum = 0
for i in queue:
    sum += i
# 출력
print(sum)