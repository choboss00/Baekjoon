import sys

num_list = [0 for i in range(0, 10)]

for i in range(0,10):
    num_list[i] = int(sys.stdin.readline().strip())

div_list = []

for i in num_list:
    div_list.append(i % 42)

print(len(set(div_list)))