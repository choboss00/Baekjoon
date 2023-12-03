"""
문제 : GCD 합
1. 가능한 모든 쌍의 GCD 합 구하는 프로그램 작성하기

"""
import sys
import math

def back(length, depth, level):
    if len(check_list) == depth:
        ans_list.append(math.gcd(*check_list))
        return

    for i in range(level, length):
        check_list.append(n_list[i])
        back(length, depth, i+1)
        check_list.pop()

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n_list = list(map(int, input().split()))[1:]
    check_list = []
    ans_list = []
    # depth, level
    back(len(n_list), 2, 0)

    print(sum(ans_list))

