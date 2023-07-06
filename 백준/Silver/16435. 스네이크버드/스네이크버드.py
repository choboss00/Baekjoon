"""
16435번. 스네이크버드 ( 실버 5 )

"""
import sys

input = sys.stdin.readline

n, l = map(int, input().split())
n_list = sorted(list(map(int, input().split())))

for i in n_list:
    if l >= i:
        l += 1

print(l)
