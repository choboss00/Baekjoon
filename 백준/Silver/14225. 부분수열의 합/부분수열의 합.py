import sys

input = sys.stdin.readline

n = int(input())

a = 0

n_list = list(map(int, input().split()))

n_list.sort()

for i in n_list:
    if a + 1 < i:
        break
    a += i

print(a+1)