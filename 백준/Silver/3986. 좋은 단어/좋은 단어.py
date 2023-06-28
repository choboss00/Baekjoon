"""
3986번 : 좋은 단어

좋은 단어 기준 : 단어 위로 아치형 곡선을 그어 같은 글자끼리 쌍
선끼리 교차하지 않으면서 각 글자를 정확히 한 개의 다른 위치에 있는
같은 글자와 짝 지을수 있다면, 좋은 단어

ABAB -> 좋은 단어 X
AABB, ABBA -> 좋은 단어 O
즉, 가장 먼저 나온 단어는 바로 사라지거나, 아니면 2번 3번 문자가 들어와서 사라지는 경우

"""
import sys
from collections import deque
input = sys.stdin.readline

# 입력받기
n = int(input())
answer = 0
for i in range(n):
    # stack
    stack = deque()
    # 좋은 단어 인 경우 찾기
    s = deque(input().strip())
    while s:
        l = s.popleft()
        # 스택이 비었을 때
        if len(stack) == 0:
            stack.append(l)
        else:
            # A A 일 경우
            if stack[-1] == l:
                stack.pop()
            else:
                stack.append(l)

    if len(stack) == 0:
        answer += 1
print(answer)
