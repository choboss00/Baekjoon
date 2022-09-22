import sys

N = int(sys.stdin.readline().strip())
N_list = list(map(int, sys.stdin.readline().split()))
N_list.sort()
N_list_value = [0 for i in range(N)]

M = int(sys.stdin.readline().strip())
M_list = list(map(int, sys.stdin.readline().split()))

dic = dict(zip(N_list, N_list_value))

for i in M_list:
    if i in dic:
        print(1)
    else:
        print(0)

