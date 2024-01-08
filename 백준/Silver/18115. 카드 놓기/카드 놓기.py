"""
## 18115번 : 카드 놓기

## 문제
1. 손에 들린 카드를 하나씩 내려놓아 바닥에 쌓으려고 함

2. 사용할 수 있는 기술
- 제일 위의 카드 1장을 바닥에 내려놓기
- 위에서 두번째 카드를 바닥에 내려놓기 ( 카드가 2장 이상일 때만 사용 가능 )
- 제일 밑에 있는 카드를 바닥에 내려놓기 ( 카드가 2장 이상일 때만 사용 가능 )

3. 처음에 N장의 카드를 들고 있으며, 카드에는 1부터 N까지의 정수가 중복되지 않게 적혀있음

4. 기술을 N번 사용하여 카드를 다 내려놓았을 때, 놓여 있는 카드를 확인했더니 순서대로 1 ~ N 이 적혀있었음

5. 처음 카드의 상태 출력하기

## 입력
1. N, 길이가 N 인 수열 A
- Ai 가 x 이면, i번째로 카드를 내려놓을 때 x번 기술을 사용했다는 뜻
- Ai 는 1, 2, 3 중 하나이며, An 은 항상 1임 ( 마지막 숫자는 항상 1 )

## 출력
1. 초기 카드의 상태를 위에서부터 순서대로 출력하기

## 풀이
1. 현재 상태 : 1, 2, 3, ... N 까지 순서대로 놓아져 있다.

2. 초기 카드의 상태를 맞추기 위해, 문제에 맞게 리스트의 값들을 변경해줄 필요가 있음

"""
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

n_list = list(map(int, input().split()))

n_list.reverse()

queue = deque()

for i in range(n):
    if n_list[i] == 1:
        queue.append(i+1)
    elif n_list[i] == 2:
        x = queue.pop()
        queue.append(i+1)
        queue.append(x)
    else:
        queue.appendleft(i+1)

queue.reverse()

print(*queue)
