"""
## Z

## 문제
1. 크기 : 2^N * 2^N 인 2차원 배열

2. 이 배열을 Z모양으로 탐색하려고 함
- 방향 : 오른쪽, 왼쪽아래, 오른쪽, 오른쪽위

3. N 이 1 보다 큰 경우, 배열을 크기가 2^(N-1) * 2^(N-1) 로 4등분 한 후 재귀적으로 순서대로 방문함

4. N 의 크기가 1이 될 때 까지 재귀적으로 반복하며 배열을 쪼갬

## 입력
1. 정수 N, r, c

2. 1 <= N <= 15

3. r >= 0, c < 2^N

## 출력
1. r행 c열을 몇 번째로 방문했는지 출력하기

## 풀이
1. 좌표를 넣어줘야 함
- 어떤 좌표냐하면, 쪼갰을 때 가장 처음에 시작하는 좌표

2. 예시 ( N = 3 )
- (4,4) 에서 시작 ( 2^(N-1) )
- (4,0), (0,4), (4,4)
- 좌표 중 하나가 0 인 경우, (4,0), (6,0), (4,2), (6,2) 가 돼야 함
- 2^N 을 한번 더 2로 나눈뒤, (2,0), (0,2), (2,2), (4,0), (0,4), (4,4)
- 2^N 을 한번 더 2로 나누면, 1 이므로 중단, 아까 넣을 때 (0,0) 도 같이 넣어줌
-
"""
import sys

def Z(N, r, c):
    if r == 0 and c == 0:
        return 0
    elif r == 0 and c == 1:
        return 1
    elif r == 1 and c == 0:
        return 2
    elif r == 1 and c == 1:
        return 3

    NN = 2 ** (N-1) # 보드 분할
    s = NN ** 2 # 보드의 값

    if r < NN and c < NN:
        return Z(N-1, r, c)
    elif r < NN and c >= NN:
        return s + Z(N-1, r, c-NN)
    elif r >= NN and c < NN:
        return s * 2 + Z(N-1, r-NN, c)
    elif r >= NN and c >= NN:
        return s * 3 + Z(N-1, r-NN, c-NN)

input = sys.stdin.readline

N, r, c = map(int, input().split())

print(Z(N,r,c))


