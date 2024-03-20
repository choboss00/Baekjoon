"""
## 신기한 소수

## 문제
1. N 자리의 숫자 중에서 어떤 수들이 신기한 소수인지 궁금해졌음

2. N이 주어졌을 때, N자리 신기한 소수 모두 찾기

## 입력
1. N

## 출력
1. N자리 수 중에서 신기한 소수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하기

## 풀이
1. 유망 함수 정의
- 소수 판별

"""

import sys
import math
input = sys.stdin.readline

N = int(input())
ans = []

def primenumber(x):
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True

def back(num, s):
    if len(s) == num:
        if primenumber(int(s)):
            ans.append(s)
        return

    for i in range(10):
        s = s + str(i)
        if primenumber(int(s)):
            back(num, s)
        s = s[:len(s)-1]

back(N, '2')
back(N,'3')
back(N, '5')
back(N, '7')


for a in ans:
    print(a)

