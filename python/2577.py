import sys

num_list = [0 for i in range(0,3)]
number = 1
for i in range(0,3):
    num_list[i] = int(sys.stdin.readline().strip())
    number *= num_list[i]

result_list = list(str(number))

dic = {}

for i in "0123456789":
    dic[i] = 0

for i in result_list:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in dic.values():
    print(i)