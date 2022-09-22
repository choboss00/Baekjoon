import sys
from collections import deque

# N장의 카드 받기
N = int(sys.stdin.readline().strip())
N_list= deque([i for i in range(1,N+1)])

# 반복 len(N_list) != 1 일때
while(len(N_list) != 1):
    # 제일 위에 있는 카드를 버리기
    N_list.popleft()
    # 그 다음 카드를 제일 아레에 있는 카드 밑으로 옮기기
    N_list.append(N_list[0])
    N_list.popleft()
# 마지막에 남는 카드 구하기
print(N_list[0])