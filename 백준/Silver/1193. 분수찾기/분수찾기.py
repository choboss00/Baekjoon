"""
## 분수찾기

## 문제
1. 무한히 큰 배열에 분수들이 적혀있음

2. x 가 주어졌을 때, x 번째 분수를 구하는 프로그램 작성하기

## 입력
1. x

## 출력
1. 분수 출력

## 풀이
1. 규칙 찾기
"""
import sys

input = sys.stdin.readline

x = int(input())

for i in range(1, 20000):
    num = i * (i+1) // 2

    if x > num:
        continue
    elif x == num:
        if i % 2 == 1: # 홀수일 때
            print(f'1/{i}')
        else:
            print(f'{i}/1')
        break
    else: # x 가 더 작은경우
        idx = num - x
        if i % 2 == 1:
            print(f'{1+idx}/{i-idx}')
        else:
            print(f'{i-idx}/{1+idx}')
        break


