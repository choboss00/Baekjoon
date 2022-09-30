import sys

N = int(sys.stdin.readline().strip())
N_list = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline().strip())

cnt = 0
N_list.sort()

start, end = 0, N-1

while start < end:
    # 가장 작은 값과 가장 큰값을 더해서 x값과 비교하기
    interval_sum = N_list[start] + N_list[end]
    if(interval_sum == x):
        cnt += 1
        start += 1
        end -= 1
    # 값이 작을 때
    elif interval_sum < x:
        start += 1
    # 값이 클 때
    else:
        end -= 1

print(cnt)