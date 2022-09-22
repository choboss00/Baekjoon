import sys

N = int(sys.stdin.readline().strip())
num_list = list(map(int, sys.stdin.readline().split()))
count = 0
num = 0
for i in num_list:
    if(i == 2):
        count += 1
    if(i > 2):
        for j in range(2, i):
            if(i % j == 0):
                break
            num = j
        if(i == num+1):
            count += 1


print(count)