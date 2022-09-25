import sys
from collections import deque

#M, N값 받기
M, N = map(int, sys.stdin.readline().split())
# 리스트 저장
num_list = list(map(int, sys.stdin.readline().split()))

# 큐 생성
Queue = deque([i for i in range(1, M+1)])
# 큐의 0번째 값과 리스트 값이 같으면, pop
# 리스트 값과 비교해서, 왼쪽부터 세주기
# 리스트 값과 비교해서 오른쪽부터 세주기
res_cnt = 0
for j in range(N):
    cnt_left = 0
    cnt_right = 1
    i_l = 0
    i_r = len(Queue) - 1
    while(Queue[i_l] != num_list[j]):
        cnt_left += 1
        i_l += 1
    while(Queue[i_r] != num_list[j]):
        cnt_right += 1
        i_r -= 1
    if(cnt_left > cnt_right):
        min_num = cnt_right
    else:
        min_num = cnt_left

    cnt = 0
    check_num = min_num
    while(check_num != 0):
        if(min_num == cnt_right):
            cnt += 1
            Queue.insert(0, Queue[len(Queue)-1])
            del Queue[len(Queue)-1]
        else:
            cnt += 1
            Queue.append(Queue[0])
            del Queue[0]
        check_num -= 1
    Queue.popleft()
    res_cnt += cnt
print(res_cnt)