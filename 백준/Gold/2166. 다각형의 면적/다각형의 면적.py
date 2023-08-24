
import sys

input = sys.stdin.readline

n = int(input())
xy_list = []

for _ in range(n):
    x,y = map(int, input().split())

    xy_list.append([x,y])

xy_list.append([xy_list[0][0],xy_list[0][1]])

n1 = 0
n2 = 0

for i in range(n):
    n1 += xy_list[i][0] * xy_list[i+1][1]
    n2 += xy_list[i][1] * xy_list[i+1][0]

ans = abs(n1 - n2) / 2

print(round(ans, 1))