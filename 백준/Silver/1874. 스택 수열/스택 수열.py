import sys

# 숫자 n 받기
n = int(sys.stdin.readline().strip())
# 수열 리스트 만들기
n_list = [int(sys.stdin.readline().strip()) for i in range(0, n)]
# 스택 만들기
stack = []
stack_cnt = 1
res_list = []
check = 0

# 스택수열 만들기
for i in range(0, n):
    # 값이 더 작을경우 push
    while(stack_cnt <= n_list[i]):
        stack.append(stack_cnt)
        res_list.append("+")
        stack_cnt += 1
    # pop
    if(stack[-1] == n_list[i]):
        res_list.append("-")
        stack.pop()
    else:
        print("NO")
        check = 1
        break
# 결과 출력
if(check == 0):
    for i in range(len(res_list)):
        print(res_list[i])