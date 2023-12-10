"""
## 2501번 : 약수 구하기
## 문제
1. 두 개의 자연수 N, K 가 주어졌을 때 N 의 약수들 중 K번째로 작은 수 출력하기

## 입력
1. N, K

## 출력
1. N 의 약수들 중 K 번째로 작은 수 출력하기
- N 의 약수의 개수가 K 보다 작아서 K 번째의 약수가 존재하지 않을 경우 0 출력

## 풀이
1. 약수 구하기
"""
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

n_list = [] # 약수를 저장할 리스트


for i in range(1, n+1):
    if n % i == 0:
        n_list.append(i)

if len(n_list) >= k:
    print(n_list[k-1])
else:
    print(0)

