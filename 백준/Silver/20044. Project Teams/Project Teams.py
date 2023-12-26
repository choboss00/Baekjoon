"""
## 20044번 : Project Teams

## 문제
1. 프로젝트 팀 하나는 두명의 학생으로 구성됨

2. 팀원 코딩 역략의 합을 최대한 일정하게 유지하려고 함

3. 학생들의 코딩 역량이 주어졌을 때 팀 구성하는데 도움이 되는 프로그램 작성하기

## 입력
1. 팀 수 n

2. 코딩 역량을 나타내는 양의 정수
- 학생들의 코딩 역량은 모두 다름

## 출력
1. Sm 출력
- min(w(Gi)) 가 최대인 값

## 풀이
1. 정렬 후 합친 뒤 가장 작은 값 찾기

1 2 3 5 7 9
"""
import sys

input = sys.stdin.readline

n = int(input())

n_list = list(map(int, input().split()))

n_list.sort()

_min = 222222

for i in range(n):
    if n_list[i] + n_list[n * 2 - i - 1] < _min:
        _min = n_list[i] + n_list[n * 2 - i - 1]

print(_min)
