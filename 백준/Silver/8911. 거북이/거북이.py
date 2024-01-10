"""
## 8911번 : 거북이

## 문제
1. 명령
- F : 앞으로 한칸
- B : 뒤로 한칸
- L : 왼쪽으로 90도 회전
- R : 오른쪽으로 90도 회전

2. 거북이가 이동한 영역을 계산해보려고 함

3. 거북이가 지나간 영역을 모두 포함할 수 있는 가장 작은 직사각형의 넓이를 구하는 프로그램 작성하기
- 초기 위치 : (0, 0)
- 북쪽을 바라보고 있음

## 입력
1. 테스트 케이스 T

## 출력
1. 거북이가 이동한 영역을 모두 포함하는 가장 작은 직사각형의 넓이 출력

## 풀이
1. 거북이가 이동한 가로, 세로 길이 구하기
"""
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    # 방향 체크 ( 0 : 북, 1 : 서, 2 : 남, 3 : 동 )
    d = 0 # 초기 방향

    # 초기 위치
    x, y = 500, 500

    # x 의 최대, 최소와 y 의 최대, 최소를 저장
    x_min, x_max, y_min, y_max = 500, 500, 500, 500

    ctls = input().strip()

    for ctl in ctls:
        if ctl == 'L':
            if d == 3:
                d = 0 # 북으로 방향 변경
            else:
                d += 1 # 방향 이동
        elif ctl == 'R':
            if d == 0:
                d = 3 # 동으로 방향 변경
            else:
                d -= 1 # 방향 이동
        elif ctl == 'F':
            if d == 0: # 위로 이동
                y += 1
            elif d == 1:
                x -= 1
            elif d == 2:
                y -= 1
            elif d == 3:
                x += 1
        elif ctl == 'B':
            if d == 0:
                y -= 1
            elif d == 1:
                x += 1
            elif d == 2:
                y += 1
            elif d == 3:
                x -= 1

        if x_min > x:
            x_min = x
        if x_max < x:
            x_max = x
        if y_min > y:
            y_min = y
        if y_max < y:
            y_max = y

    가로 = abs(x_max - x_min)
    세로 = abs(y_max - y_min)
    
    print(가로 * 세로)




