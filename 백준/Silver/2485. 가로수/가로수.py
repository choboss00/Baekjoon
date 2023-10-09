import sys
import math

input = sys.stdin.readline

n = int(input())

n_list = [int(input()) for _ in range(n)]

d_list = []

for i in range(n-1):
    d_list.append(n_list[i+1] - n_list[i])

# 최대 공약수 구하기
GCD = math.gcd(*d_list)

# 정답
ans = 0

checkNum = n_list[0]

for j in range(1, n):
    checkNum += GCD
    if checkNum == n_list[j]:
        continue
    else:
        a, b = divmod(n_list[j], GCD)
        c, d = divmod(checkNum, GCD)
        ans += a - c
        checkNum = n_list[j]


print(ans)