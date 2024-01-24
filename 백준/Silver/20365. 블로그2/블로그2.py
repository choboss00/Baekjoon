"""
## 블로그2

## 문제
1. 문제 색칠 작업
- 연속된 임의의 문제들을 선택함
- 선택된 문제들을 전부 원하는 같은 색으로 칠하기

## 입력
1. 색을 칠해야 하는 문제의 수 N

2. 문자
- R : 빨강, B : 파랑

## 출력
1. 모든 문제를 원하는 색으로 칠할 때 까지 필요한 작업 횟수의 최솟값 출력

## 풀이
1. 칠해야하는 수가 많은 색깔로 하나로 밀기

2. 반대되는 색깔 칠하기

"""
import sys

input = sys.stdin.readline

n = int(input())
colors = input().strip()

stack = []

first_color = colors[0] # 첫번째 색

s = ''
# 색깔 수 초기화
red, blue = 0, 0

for color in colors:
    if first_color == color:
        s += color
        continue

    if first_color == 'R': # RED
        red += 1
    else:
        blue += 1

    stack.append(s)
    # 초기화
    first_color = color
    s = ''
    s += color

# 마지막 색깔 넣기
stack.append(s)
if first_color == 'R':  # RED
    red += 1
else:
    blue += 1

if red < blue: # red 수가 더 적을 경우
    print(1 + red)
else:
    print(1 + blue)
