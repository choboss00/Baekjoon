"""
11899번. 괄호 끼워넣기
"""
import sys
from collections import deque

input = sys.stdin.readline

n = input().strip()
q = deque()

# 문자열 길이
l = len(n)

# 거꾸로 넣기
for i in range(l-1, -1, -1):
    q.appendleft(n[i])

    if len(q) >= 2 and q[0] == '(' and q[1] == ')':
        q.popleft()
        q.popleft()

print(len(q))
