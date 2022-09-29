import sys
from collections import deque
# 입력값 받기
N = int(sys.stdin.readline().strip())
# Queue
q = deque([])

# N번 반복 명령 작성 (push, pop, size, empty, front, back)
for i in range(N):
    N_List = sys.stdin.readline().split()
    # push
    if(N_List[0] == "push"):
        q.append(N_List[1])
    # pop
    elif(N_List[0] == "pop"):
        # 큐에 정수가 존재
        if(len(q) != 0):
            print(q.popleft())
        # 없을 때
        else:
            print(-1)
    # size
    elif(N_List[0] == "size"):
        print(len(q))
    # empty
    elif(N_List[0] == "empty"):
        if(len(q) == 0):
            print(1)
        else:
            print(0)
    # front
    elif(N_List[0] == "front"):
        if(len(q) != 0):
            print(q[0])
        else:
            print(-1)
    # back
    elif(N_List[0] == "back"):
        if(len(q) != 0):
            print(q[len(q)-1])
        else:
            print(-1)