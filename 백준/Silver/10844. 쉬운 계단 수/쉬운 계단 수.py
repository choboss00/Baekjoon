"""
## 쉬운 계단 수

## 문제
1. 인접한 모든 자리의 차이가 1인 수를 계단 수 라고 함
- 그래프 알고리즘으로 문제 접근 ( 완전 탐색 )
- DP 로 접근

2. N 이 주어질 때, 길이가 N 인 계단 수가 총 몇개 있는지 구해보기

## 입력
1. 첫째 줄에 N 이 주어짐
- N 은 100보다 작거나 같은 자연수

## 출력
1. 정답을 10억으로 나눈 나머지 출력하기

## 풀이
1. DP
- 이전 자릿수까지 얼마나 많은 계단 수가 존재했는지 저장하기

2. 백트래킹

"""
import sys

input = sys.stdin.readline

# 길이
N = int(input())

dp = [[0 for _ in range(10)] for _ in range(N)]

# 첫번째 자릿수
for i in range(1, 10):
    dp[0][i] = 1

for i in range(1, N):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[N-1]) % 1000000000)
