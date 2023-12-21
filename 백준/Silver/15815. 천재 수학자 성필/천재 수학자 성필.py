"""
## 15815번 : 천재 수학자 성필

## 문제
1. 연산자 우선순위에 따라 식 변경하기

## 입력
1. 길이가 100이 넘지 않는 수식

## 출력
1. 답 출력

## 풀이
1. 스택

"""
import sys

input = sys.stdin.readline

수식 = list(input().strip())

수식.reverse()

stack = []

while 수식:
    값 = 수식.pop()

    if 값 == '+':
        stack.append(stack.pop() + stack.pop())
    elif 값 == '-':
        a = stack.pop()
        b = stack.pop()
        stack.append(b - a)
    elif 값 == '*':
        stack.append(stack.pop() * stack.pop())
    elif 값 == '/':
        a = stack.pop()
        b = stack.pop()
        stack.append(b // a)
    else:
        stack.append(int(값))

print(*stack)
