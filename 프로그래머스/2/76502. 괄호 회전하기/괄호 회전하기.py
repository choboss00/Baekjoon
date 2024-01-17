from collections import deque

def solution(s):
    answer = 0
    queue = deque(s)
    
    x = len(s) # 회전 수
    
    stack = []
    
    for q in queue:
        if len(stack) == 0: # 스택이 비어있을 때
            stack.append(q)
            continue
        
        # 스택의 마지막 원소와 큐의 원소 비교
        if stack[-1] == '(' and q == ')':
            stack.pop()
        elif stack[-1] == '[' and q == ']':
            stack.pop()
        elif stack[-1] == '{' and q == '}':
            stack.pop()
        else:
            stack.append(q)
    
    if len(stack) == 0:
        answer += 1
    
    for i in range(1, x):
        stack = []
        queue.rotate(-1)
        for q in queue:
            if len(stack) == 0: # 스택이 비어있을 때
                stack.append(q)
                continue

            # 스택의 마지막 원소와 큐의 원소 비교
            if stack[-1] == '(' and q == ')':
                stack.pop()
            elif stack[-1] == '[' and q == ']':
                stack.pop()
            elif stack[-1] == '{' and q == '}':
                stack.pop()
            else:
                stack.append(q)

        if len(stack) == 0:
            answer += 1
    
    return answer

"""
## 괄호 회전하기

## 문제
1. (), [], {} => 올바른 괄호 문자열

2. s 를 왼쪽으로 x 칸만큼 회전시켰을 때, s 가 올바른 괄호 문자열이 되게 하는 
  x 의 개수를 return 하는 함수 만들기

## 풀이
1. s-1 번만큼 왼쪽으로 rotate 했을 때, 올바른 괄호 문자열이 되는지 체크하기
"""