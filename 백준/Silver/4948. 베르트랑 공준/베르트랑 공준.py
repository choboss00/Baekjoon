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

input = sys.stdin.readline

def prime(n):
    cnt = 0
    arr = [0 for _ in range(n+1)]

    for i in range(2, n+1):
        if arr[i] == 0:
            cnt += 1
            for j in range(i, n+1, i):
                arr[j] = 1 # 소수가 아니기 때문에 처리해줌
    return cnt

while True:
    n = int(input())

    if n == 0:
        break

    print(prime(n * 2) - prime(n))