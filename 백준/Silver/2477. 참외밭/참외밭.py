import sys

K = int(sys.stdin.readline().strip())

lst = []
# 리스트에 값 집어넣기
for i in range(6):
    M, N = map(int, sys.stdin.readline().split())
    lst.append(N)

max_num = 0
min_num = 0
idx = 0

for i in range(6):
    tmp = lst[i] * lst[(i+1) % 6]
    if (max_num < tmp):
        max_num = tmp
        idx = i
min_num = lst[(idx + 3) % 6] * lst[(idx + 4) % 6]
print(K * (max_num - min_num))