import sys

input = sys.stdin.readline

n,k = map(int, input().split())

n_list = []

for _ in range(n):
    n_list.append(int(input()))

le, ri = 1, max(n_list)
res = 0
while le <= ri:
    s = 0
    mid = (le+ri)//2

    for i in range(n):
        s += (n_list[i] // mid)

    if s >= k:
        le = mid + 1
        res = mid
    else:
        ri = mid - 1

print(res)