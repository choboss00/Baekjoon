"""
17952번. 과제는 끝나지 않아!

1. 과제는 가장 최근에 나온 순서대로
2. 받으면 바로 시작
3. 과제를 하던 도중 새로운 과제가 나오면 새로운 과제 진행
3. 새로운 과제가 끝났다면, 이전에 하던 과제를 이어서 진행

1) 입력값 받기
2) 0 -> 없음 / 1 -> 과제 있음
3) A : 과제의 점수, T : 과제를 해결하는데 걸리는 시간

다음 과제가 0 이면 -> 이전 과제 진행
그렇지 않으면 넘어가기
스택 구조 -> 스택 활용. 스택에 담아놓기!

"""

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
stack = deque()
ans = 0
for i in range(n):
    a_list = list(map(int, input().split()))
    # 과제 있음
    if a_list[0] == 1:
        stack.append([a_list[1], a_list[2]])

    if stack:
        s, t = stack.pop()

        t -= 1
        if t == 0:
            ans += s
        else:
            stack.append([s,t])

print(ans)