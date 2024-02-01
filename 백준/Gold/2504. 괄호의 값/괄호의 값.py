"""
## 괄호의 값

## 문제
1. 4개의 기호 : (, ), [, ] 를 이용해서 만들어지는 괄호열 중 올바른 괄호열 정의
- (), [] : 올바른 괄호열
- 만일 x 가 올바른 괄호열일경우, (x), [x] 도 모두 올바른 괄호열이 됨
- x, y 모두 올바른 괄호열이라면 이들을 결합한 xy 도 올바른 괄호열이 됨

2. 어떤 올바른 괄호열 x 에 대하여 그 괄호열의 값을 아래와 같이 정의하고 값 ( x ) 으로 표시함
- () : 값 2
- [] : 값 3
- (x) : 2 * 값(x)
- [x] : 3 * 값(x)
- xy : x + y

3. 예시 : (()[[]])([])
- ()[[]] : 2 + 3 * 3 = 11 ( x )
- ( x ) : 2 * 11 = 22
- x ([]) = 22 + 3 * 2 = 28

## 입력
1. 첫째 줄에 괄호열을 나타내는 문자열이 주어짐

## 출력
1. 그 괄호열의 값을 나타내는 정수 출력하기
- 입력이 올바르지 못한 경우, 0 출력

## 풀이
1. 예시 : [[]]
- [] -> 3 으로 변환
- [, 3, ] -> 안에 숫자가 있으니, 3 * 3 = 9

2. 즉 stack 을 쌓을 때, 마지막 원소가 숫자다 -> 이미 변환된 값
- 그러므로, 마지막보다 이전 값과 비교할 필요가 있음

3. 순서
- stack 을 만든다
- stack 의 마지막 원소와 현재 담으려고 하는 원소를 비교한다
- 만약 괄호열이 일치하는 경우, 숫자로 변환해서 stack 에 담는다
- 만약 마지막 원소가 숫자인 경우, stack 의 이전 값과 비교해서 괄호열 체크한다
- 괄호열이 일치하는 경우, () 인지 [] 인지에 맞춰서 마지막 원소의 숫자와 곱해준다
- 만약 마지막 원소와 마지막보다 이전 원소가 숫자인 경우, 두 숫자를 더해준다
"""
import sys
from collections import deque

input = sys.stdin.readline

stack = deque()

queue = deque(input().strip())

while queue:
    s = queue.popleft() # 첫번째 원소
    # 원소가 하나도 없을 경우
    if len(stack) == 0:
        stack.append(s)
        continue

    # ( xy = x + y )
    if len(stack) > 2 and type(stack[-1]) == int and type(stack[-2]) == int:
        stack.append(stack.pop() + stack.pop())
        if stack[-2] == '(' and s == ')':
            num = stack.pop()
            stack.pop() # 필요없는 괄호 제거
            stack.append(2 * num)
        elif stack[-2] == '[' and s == ']':
            num = stack.pop()
            stack.pop() # 필요없는 괄호 제거
            stack.append(3 * num)
        else:
            stack.append(s)
    # stack 의 마지막 원소만 숫자일 경우
    elif len(stack) >= 2 and type(stack[-1]) == int:
        if stack[-2] == '(' and s == ')':
            num = stack.pop()
            stack.pop() # 필요없는 괄호 제거
            stack.append(2 * num)
        elif stack[-2] == '[' and s == ']':
            num = stack.pop()
            stack.pop() # 필요없는 괄호 제거
            stack.append(3 * num)
        else:
            stack.append(s)
    # stack 의 첫번째 원소만 숫자일 경우
    elif len(stack) == 1 and type(stack[-1]) == int:
        stack.append(s)
    # 나머지 케이스
    else:
        if stack[-1] == '(' and s == ')':
            stack.pop() # 필요없는 괄호 제거
            stack.append(2)
        elif stack[-1] == '[' and s == ']':
            stack.pop() # 필요없는 괄호 제거
            stack.append(3)
        else:
            stack.append(s)


ans = 0

for s in stack:
    if type(s) == int:
        ans += s
    else:
        print(0)
        exit(0)
print(ans)


