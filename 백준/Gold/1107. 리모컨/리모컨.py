"""
1107번 : 리모컨

## 문제
1. 일부 숫자 버튼이 고장남

2. 리모컨
- 버튼 : 0 ~ 9, +, 0
- + : 현재 채널에서 +1 된 채널로 이동
- - : 현재 채널에서 -1 된 채널로 이동
- 채널 0 에서 0 를 누른 경우, 채널 이동 X ( 음수 이동 x )

3. 수빈이가 지금 이동하려고 하는 채널 : N

4. 어떤 버튼이 고장났는지 주어졌을 때, 채널 N 으로 이동하기 위해서
버튼을 최소 몇번 눌러야하는지 구하는 프로그램 작성하기

5. 현재 채널 : 100

## 입력
1. 이동하려고 하는 채널 : N

2. 고장난 버튼의 갯수 M

## 출력
1. 채널 N 으로 이동하기 위해 버튼을 최소 몇번 눌러야하는지 구하기

"""
import sys

input = sys.stdin.readline

N = input().strip() # 이동할 채널
M = int(input()) # 고장난 갯수
now = abs(100 - int(N))

if M != 0:
    M_list = set(map(int, input().split()))  # 고장 집합
else:
    M_list = set()

for i in range(1000001):
    i_set = set(map(int, str(i)))

    if len(M_list & i_set) == 0: # 고장 집합과의 교집합
        now = min(now, abs(int(N)-i) + len(str(i)))

print(now)