"""

## 12789번 : 도키도키 간식드리미

## 문제
1. 모든 사람들이 순서대로 간식을 받을 수 있는지 확인하는 프로그램 만들기

2. 현재 1열로 줄 서있고, 맨 앞의 사람만 이동 가능

3. 번호표 순서대로만 통과할 수 있는 라인 존재

4. 이 라인과 대기열의 맨 앞사람 사이에는 한 사람씩 1열이 들어갈 수 있는 공간이 있음
- 대기열의 사람들은 이 공간으로 들어올 수 있지만 반대는 불가능함

## 입력
1. 승환이의 앞에 서있는 학생들의 수 N

2. 모든 학생들의 번호표

## 출력
1. 무사히 간식을 받을 수 있으면 -> Nice

2. 그렇지 않다면 Sad

## 풀이
1. 큐 2개 활용하기

2. 번호표 순서에 안맞을 경우 -> 다른 큐에 임시 저장
-
"""
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

n_queue = deque(map(int, input().split())) # 학생들의 번호표
sub_queue = deque() # 한명씩만 들어갈 수 있는 공간

idx = 1 # 학생들의 번호표 체크

while n_queue:
    nq= n_queue.popleft()
    # 번호표 순서에 맞을 경우
    if idx == nq:
        idx += 1
        continue
    # 서브 큐에서 나갈 수 있을 때
    if len(sub_queue) > 0:
        sub = sub_queue.pop()
        if sub == idx:
            idx += 1
            n_queue.appendleft(nq)
            continue
        sub_queue.append(sub)

    sub_queue.append(nq)

while sub_queue:
    sub2 = sub_queue.pop()

    if sub2 == idx:
        idx += 1
        continue
    else:
        break

if len(sub_queue) == 0:
    print("Nice")
else:
    print("Sad")