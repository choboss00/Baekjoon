import sys

N = int(sys.stdin.readline().strip())

OX_list = [sys.stdin.readline().strip() for i in range(N)]

for i in range(N):
    sum = 0
    count = 0
    for j in range(0, len(OX_list[i])):
        if(OX_list[i][j] == 'O'):
            count += 1
            sum += count
        else:
            count = 0
    print(sum)
