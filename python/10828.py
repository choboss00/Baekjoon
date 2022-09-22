import sys

N = int(sys.stdin.readline().strip())
list = [list(sys.stdin.readline().split()) for i in range(N)]

stack = []

for i in range(0, len(list)):
    if(list[i][0] == "push"):
        stack.append(int(list[i][1]))
    elif(list[i][0] == "pop"):
        if(len(stack) == 0):
            print(-1)
        else:
            print(stack.pop())
    elif(list[i][0] == "size"):
        print(len(stack))
    elif(list[i][0] == "empty"):
        if(len(stack) == 0):
            print(1)
        else:
            print(0)
    elif(list[i][0] == "top"):
        if(len(stack) == 0):
            print(-1)
        else:
            print(stack[len(stack)-1])