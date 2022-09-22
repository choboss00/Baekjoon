import sys

N = int(sys.stdin.readline())
list_1 = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
list_2 = list(map(int, sys.stdin.readline().split()))

dict = {}

for i in range(len(list_1)):
    dict[list_1[i]] = 0


for i in range(M):
    if list_2[i] not in dict:
        print(0, end=' ')
    else:
        print(1, end=' ')

