import sys

input = sys.stdin.readline

h,w,x,y = map(int, input().split())

b_list = []

for _ in range(h+x):
    b_list.append(list(map(int, input().split())))

for i in range(x, h+x):
    for j in range(y, w+y):
        b_list[i][j] = b_list[i][j] - b_list[i-x][j-y]


for i in range(h):
    for j in range(w):
        print(b_list[i][j], end=' ')
    print()