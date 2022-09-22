import sys
from collections import deque
N = int(sys.stdin.readline().strip())
queue_list = list(sys.stdin.readline().split() for i in range(N))
queue = deque([])

for i in range(N):
    if(queue_list[i][0] == "push"):
        queue.append(int(queue_list[i][1]))
    elif(queue_list[i][0] == "pop"):
        if(len(queue) != 0):
            print(queue.popleft())
        else:
            print(-1)
    elif(queue_list[i][0] == "size"):
        print(len(queue))
    elif(queue_list[i][0] == "empty"):
        if(len(queue) == 0):
            print(1)
        else:
            print(0)
    elif(queue_list[i][0] == "front"):
        if(len(queue) != 0):
            print(queue[0])
        else:
            print(-1)
    elif(queue_list[i][0] == "back"):
        if(len(queue) != 0):
            print(queue[len(queue) - 1])
        else:
            print(-1)
