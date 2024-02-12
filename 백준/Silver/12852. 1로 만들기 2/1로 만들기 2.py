"""
## 1로 만들기 2

## 문제
1. 정수 X 에 사용할 수 있는 연산
- X 가 3 으로 나누어 떨어지면, 3 으로 나누기
- X 가 2 로 나누어 떨어지면, 2로 나누기
- X 에 1 빼기

2. 정수 N 이 주어졌을 때, 위와 같은 연산 3개를 적절히 사용해서 1을 만들려고 함

4. 연산을 사용하는 횟수의 최솟값 출력하기 ( BFS )

## 입력
1. 첫째 줄에 1 이상, 10^6 이하 자연수 N

## 츨력
1. 첫째 줄에 연산을 하는 횟수의 최솟값 출력

2. 둘째 줄에는 N 을 1 로 만드는 방법에 포함되어 있는 수를 공백으로 구분해서 순서대로 출력하기
- 정답이 여러가지인 경우에는 아무거나 출력

## 풀이
1. BFS

"""
import sys
from collections import deque
from copy import deepcopy

def bfs(n):
    queue = deque()

    visited = [False for _ in range(n+1)]

    queue.append([n, 0, [n]])

    while queue:
        x, cnt, sub_list = queue.popleft()

        if x == 1:
            return cnt, sub_list

        if x % 3 == 0 and not visited[x // 3]:
            l_3 = deepcopy(sub_list)
            l_3.append(x // 3)
            queue.append([x // 3, cnt + 1, l_3])
            visited[x // 3] = True
        if x % 2 == 0 and not visited[x // 2]:
            l_2 = deepcopy(sub_list)
            l_2.append(x // 2)
            queue.append([x // 2, cnt + 1, l_2])
            visited[x // 2] = True
        if not visited[x - 1]:
            l_1 = deepcopy(sub_list)
            l_1.append(x - 1)
            queue.append([x - 1, cnt + 1, l_1])
            visited[x - 1] = True

input = sys.stdin.readline

n = int(input())

ans, ans_list = bfs(n)

print(ans)
print(*ans_list)
