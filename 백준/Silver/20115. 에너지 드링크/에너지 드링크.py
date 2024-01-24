"""
## 에너지 드링크

## 문제
1. 집에 있는 에너지 드링크들을 합쳐서 한번에 마시려고 함

2. 에너지 드링크들을 합치는 과정
- 임의의 서로 다른 두 에너지 드링크를 고름
- 한쪽 에너지 드링크를 다른 쪽 에너지 드링크에 모두 붓기 ( 붓는 과정에서 원래 양의 절반을 흘림 )
- 다 붓고 남은 빈 에너지 드링크는 버림
- 위 과정을 하나의 에너지 드링크가 남을 때 까지 반복

3. 합쳐진 에너지 드링크의 양을 최대로 하는 프로그램 작성하기

## 입력
1. 가지고 있는 에너지 드링크 수 N

2. 에너지 드링크의 양

## 출력
1. 최대로 만들 수 있는 에너지 드링크의 양 출력하기
- 오차 : 10^-5 까지 허용함

## 풀이
1. 예시
- 정렬 ( 2, 3, 6, 9, 10 )
- 2, 10 -> 11
- 3, 11 -> 12.5
- 6, 12.5 -> 15.5
- 9, 15.5 -> 20

"""
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))

n_list.sort()

queue = deque(n_list)

while len(queue) > 1:
    a, b = queue.popleft(), queue.pop()

    queue.append(a / 2 + b)


print('%0.5f' %(queue[-1]))