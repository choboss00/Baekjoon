"""
## 10819번 : 차이를 최대로

## 문제
1. N개의 정수로 이루어진 배열 A

2. 배열에 들어있는 정수의 순서를 적절히 바꿔서 식의 최댓값 구하기

## 입력
1. 첫째 줄에 N 이 주어짐
- 3 <= N <= 8

2. 둘째 줄에는 배열 A 에 들어있는 정수가 주어짐
- -100 <= 배열값 <= 100

## 출력
1. 배열에 들어있는 수의 순서를 적절히 바꿔서 얻을 수 있는 식의 최댓값 출력하기

## 풀이
1. 순열
"""
from itertools import permutations
import sys

input = sys.stdin.readline

n = int(input())

permut = list(permutations(list(map(int, input().split())), n))

ans_list = []

for per in permut:
    a = 0
    for i in range(n-1):
        a += abs(per[i]-per[i+1])
    ans_list.append(a)

print(max(ans_list))