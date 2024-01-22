"""
## 톱니바퀴

## 문제
1. 4개의 톱니바퀴
- 8개의 톱니를 가지고 있음
- 톱니는 N극 또는 S극 중 하나를 나타냄
- 톱니바퀴에는 1, 2, 3, 4 번호가 매겨져있음

2. 톱니바퀴를 K번 회전시키려고 함
- 회전 : 1칸
- 시계 혹은 반시계 방향으로 회전

3. 톱니바퀴를 회전시키기 위해 회전시킬 톱니바퀴와 방향을 결정해야 함
- 톱니바퀴가 회전할 때, 서로 맞닿은 극에 따라서 옆에 있는 톱니바퀴를 회전시킬 수도 있고, 안시킬수도 있음
- 톱니바퀴 A 회전시, 그 옆에 있는 톱니바퀴 B와 서로 맞닿은 톱니의 극이 다르다면, B 는 A 가 회전한 방향과 반대방향으로 회전함

4. 예시
- 3번 톱니바퀴 : 반시계 방향으로 회전
- 회전하기 전 맞닿은 극이 다르니, 4번 톱니바퀴는 시계방향으로 회전함
- 나머지는 회전하지 않음

- 1번 톱니바퀴 : 시계 방향으로 회전
- 2번 톱니바퀴와 극이 다르니, 2번 톱니바퀴는 반시계 방향으로 회전
- 2번 톱니바퀴와 3번은 극이 다르니, 3번 톱니바퀴는 시계 방향으로 회전
- 4번은 극이 같으니 그대로 유지

5. 톱니바퀴의 초기 상태와 톱니바퀴를 회전시킨 방법이 주어졌을 때, 최종 톱니바퀴의 상태를 구하는 프로그램 작성하기

## 입력
1. 각 톱니바퀴의 상태
- 8개의 정수로 이루어져 있음
- 12시방향부터 시계방향 순서대로 주어짐
- N극 : 0, S극 : 1

2. 회전 횟수 K
- 회전시킨 톱니바퀴의 번호, 방향
- 1 : 시계 방향, -1 : 반시계 방향

## 출력
1. K번 회전시킨 이후 네 톱니바퀴의 점수의 합 구하기
- 1번 톱니바퀴의 12시 방향이 N극 : 0점, S극 : 1점
- 2번 톱니바퀴의 12시 방향이 N극 : 0점, S극 : 2점
- 3번 톱니바퀴의 12시 방향이 N극 : 0점, S극 : 4점
- 4번 톱니바퀴의 12시 방향이 N극 : 0점, S극 : 8점

## 풀이
1. 입력값 받기

2. 각 톱니바퀴 별 영향을 받는 번호
- 1번 : 2번의 7번
- 2번 : 1번의 3번, 3번의 7번
- 3번 : 2번의 3번, 4번의 7번
- 4번 : 3번의 3번

3. 차례대로 영향을 받는 톱니바퀴의 극이 같은지 확인
- 극이 같은 경우 회전하지 않음
- 극이 다른 경우, 회전하기 전 그 다음 톱니바퀴도 극 상태를 확인해야 함

4. 점수의 합 출력
"""
import sys
from collections import deque

input = sys.stdin.readline
# 톱니바퀴
queue1 = deque(input().strip())
queue2 = deque(input().strip())
queue3 = deque(input().strip())
queue4 = deque(input().strip())

# 회전
k = int(input())
rotate_list = [list(map(int, input().split())) for _ in range(k)]

for num, rotate in rotate_list:
    if num == 1: # 첫번째 톱니바퀴 : 2번의 7번과 영향
        if queue1[2] != queue2[6]: # 극이 다를경우 (1, 2)
            if queue2[2] != queue3[6]: # 극이 다를경우 (2, 3)
                if queue3[2] != queue4[6]: # 극이 다를경우 (3, 4) : 이 경우 다돌아야 함
                    queue1.rotate(rotate)
                    queue2.rotate(-rotate)
                    queue3.rotate(rotate)
                    queue4.rotate(-rotate)
                else: # 3번 4번이 같음 -> 1, 2, 3만 돌아야 함
                    queue1.rotate(rotate)
                    queue2.rotate(-rotate)
                    queue3.rotate(rotate)
            else: # 1, 2 만 돌아야 함
                queue1.rotate(rotate)
                queue2.rotate(-rotate)
        else: # 1 만 돌아야 함
            queue1.rotate(rotate)
    elif num == 2: # 2번 톱니바퀴의 경우
        check1 = False
        if queue1[2] != queue2[6]:
            check1 = True

        if queue2[2] != queue3[6]: # 2번, 3번이 다름
            if queue3[2] != queue4[6]: # 3번, 4번이 다름
                queue2.rotate(rotate)
                queue3.rotate(-rotate)
                queue4.rotate(rotate)
            else:
                queue2.rotate(rotate)
                queue3.rotate(-rotate)
        else:
            queue2.rotate(rotate)

        if check1: # 1번과 2번이 다를경우
            queue1.rotate(-rotate)
    elif num == 3: # 3번 톱니바퀴의 경우
        check4 = False
        if queue3[2] != queue4[6]: # 3, 4 가 다를경우
            check4 = True

        if queue2[2] != queue3[6]:
            if queue1[2] != queue2[6]: # 1, 2, 3 이 다돌아야함
                queue3.rotate(rotate)
                queue2.rotate(-rotate)
                queue1.rotate(rotate)
            else: # 2, 3만 돌아야 함
                queue3.rotate(rotate)
                queue2.rotate(-rotate)
        else:
            queue3.rotate(rotate)

        if check4:
            queue4.rotate(-rotate)
    else: # 4번
        if queue3[2] != queue4[6]: # 3, 4가 다를경우
            if queue2[2] != queue3[6]: # 2, 3 이 다를경우
                if queue1[2] != queue2[6]: # 1, 2가 다를경우
                    queue4.rotate(rotate)
                    queue3.rotate(-rotate)
                    queue2.rotate(rotate)
                    queue1.rotate(-rotate)
                else:
                    queue4.rotate(rotate)
                    queue3.rotate(-rotate)
                    queue2.rotate(rotate)
            else:
                queue4.rotate(rotate)
                queue3.rotate(-rotate)
        else:
            queue4.rotate(rotate)
ans = 0

if queue1[0] == '1':
    ans += 1
if queue2[0] == '1':
    ans += 2
if queue3[0] == '1':
    ans += 4
if queue4[0] == '1':
    ans += 8

print(ans)