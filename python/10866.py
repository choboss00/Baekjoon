import sys
from collections import deque

N = int(sys.stdin.readline().strip())
N_list = list(sys.stdin.readline().split() for i in range(N))
Deque = deque([])

for i in range(N):
    if(N_list[i][0] == "push_front"):
        Deque.appendleft(N_list[i][1])
    if(N_list[i][0] == "push_back"):
        Deque.append(N_list[i][1])
    if(N_list[i][0] == "pop_front"):
        if(len(Deque) != 0):
            print(Deque.popleft())
        else:
            print(-1)
    if(N_list[i][0] == "pop_back"):
        if(len(Deque) != 0):
            print(Deque.pop())
        else:
            print(-1)
    if(N_list[i][0] == "size"):
        print(len(Deque))
    if(N_list[i][0] == "empty"):
        if(len(Deque) == 0):
            print(1)
        else:
            print(0)
    if(N_list[i][0] == "front"):
        if(len(Deque) != 0):
            print(Deque[0])
        else:
            print(-1)
    if (N_list[i][0] == "back"):
        if (len(Deque) != 0):
            print(Deque[len(Deque)-1])
        else:
            print(-1)
