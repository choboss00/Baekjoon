"""
## 합분해

## 문제
1. 0 ~ N 까지의 정수 K 개를 더해서 그 합이 N 이 되는 경우의 수를 구하는 프로그램 작성하기

2. 덧셈의 순서가 바뀐 경우는 다른 경우로 셈

3. 한 개의 수를 여러 번 쓸 수 있음

## 입력
1. 두 정수 N, K

## 출력
1. 답 % 10억 나머지 출력하기

## 풀이
1. 중복조합
"""
import sys
import math

input = sys.stdin.readline

n, k = map(int, input().split())

print(math.factorial(n+k-1) // (math.factorial(n) * math.factorial(k-1)) % 1000000000)
