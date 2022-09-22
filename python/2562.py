import sys

num_list = [0 for i in range(0, 9)]

for i in range(0, 9):
    num_list[i] = int(sys.stdin.readline().strip())

max = max(num_list)
print(max)
print(num_list.index(max) + 1)