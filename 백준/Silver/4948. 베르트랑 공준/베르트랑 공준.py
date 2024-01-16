"""
## 베르트랑 공준

## 문제
1. 베르트랑 공준 : 임의의 자연수 n 에 대하여, n 보다 크고, 2n 보다 작거나 같은 소수는 적어도 하나 존재한다

2. 자연수 n 이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소스의 개수를 구하는 프로그램 작성하기

## 입력
1. 여러 개의 테스트케이스

2. 입력의 마지막에는 0이 주어짐

## 출력
1. 각 테스트 케이스에 대해서, n보다 크고 2n보다 작거나 같은 소수의 개수 출력하기

## 풀이
1. 소수 판정
"""
import sys
import math

input = sys.stdin.readline

while True:
    n = int(input())

    if n == 0:
        break
    # 소수 개수 카운트
    cnt = 0
    for i in range(n+1, 2*n+1):
        check = False
        for j in range(2, int(math.sqrt(i)+1)):
            # 나눠지는 수가 있을 경우
            if i % j == 0:
                check = True
                break
        if not check:
            cnt += 1
    print(cnt)
