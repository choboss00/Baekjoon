import sys

N = int(sys.stdin.readline().strip())
list = [sys.stdin.readline().split() for i in range(N)]

for i in range(N):
    for j in range(0, len(list[i][1])):
        print(int(list[i][0]) * list[i][1][j], end='')
    print()
