import sys

input = sys.stdin.readline

T = int(input())

n_list = [0 for _ in range(1000001)]

n_list[0] = 1
n_list[1] = 2
n_list[2] = 4

for i in range(3, 1000001):
    n_list[i] += (n_list[i-1] + n_list[i-2] + n_list[i-3]) % 1000000009

for _ in range(T):
    n = int(input())

    print(n_list[n-1])