import sys

N = int(sys.stdin.readline().strip())

num_list = sys.stdin.readline().split()

for i in range(N):
    num_list[i] = int(num_list[i])

max = max(num_list)
min = min(num_list)
print("%d %d" %(min, max))