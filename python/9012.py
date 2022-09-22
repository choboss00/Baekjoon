import sys

# list 받기
N = int(sys.stdin.readline().strip())
N_list = [list(sys.stdin.readline().split()) for i in range(N)]

# 리스트 나누기
for i in range(len(N_list)):
    stack = []
    k = 0
    stack.append(0)
    for j in range(len(N_list[i][0])):
        stack.append(N_list[i][0][j])
        if(stack[k] == '(' and stack[k+1] == ')'):
            stack.pop()
            stack.pop()
            k -= 2
        k += 1
    stack.pop(0)
    if (len(stack) == 0):
        print("YES")
    else:
        print("NO")

