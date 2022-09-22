import sys

N = int(sys.stdin.readline().strip())
num_list = list(map(int, sys.stdin.readline().split()))
new_num_list = sorted(list(set(num_list)))

dic = {new_num_list[i] : i for i in range(len(new_num_list))}

for i in num_list:
    print(dic[i], end=' ')