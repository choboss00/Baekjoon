"""
## 17626번 : Four Squares

## 문제
1. 모든 자연수는 넷 혹은 그 이하의 제곱수의 합으로 표현할 수 있다고 증명

2. 자연수 n 이 주어질 때, n 을 최소 개수의 제곱수 합으로 표현하는 컴퓨터 프로그램 작성하기

## 입력
1. 자연수 n 을 포함하는 한줄로 작성

## 출력
1. 합이 n과 같게 되는 제곱수들의 최소 개수 출력

## 풀이
1. DP
"""
import sys

input = sys.stdin.readline

n = int(input())

dp = [500001 for i in range(n+1)]

dp[0] = 0

for i in range(1, n+1):
    for j in range(1, i+1):
        val = j ** 2

        if val > i:
            break
        dp[i] = min(dp[i], dp[i - val] + 1)
print(dp[n])