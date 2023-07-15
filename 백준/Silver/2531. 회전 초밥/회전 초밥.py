"""
2531번. 회전 초밥 ( 실버 1 )

벨트 위에는 같은 종류의 초밥이 둘 이상 있을수도

두가지 행사
1. 벨트의 임이의 한 위치부터 k 개의 접시를 연속해서 먹을 경우
-> 할인

2. 초밥의 종류 하나가 쓰인 쿠폰 발생,
1번 행사에 참가할 경우 이 쿠폰에 적혀진 종류의 초밥 하나를
추가로 무료 제공
만약 이 번호에 적혀진 초밥이 현재 벨트 위에 없을 경우,
새로 만들어서 손님에게 제공

입력

첫번째 줄

회전 초밥 벨트에 놓인 접시의 수 n
초밥의 가짓수 d
연속해서 먹는 접시의 수 k -> 얘 만큼 묶어야 함
쿠폰 번호 c

둘째줄부터 회전초밥

해결
set 으로 회전초밥 받기
k 개 씩 묶기
쿠폰 번호에 적힌 초밥 빼기
"""
import sys
from collections import deque
import itertools
# 입력값
input = sys.stdin.readline

n,d,k,c = map(int, input().split())

queue = deque()
# 회전초밥 갯수 입력
for i in range(n):
    queue.append(int(input()))

# 정답
ans_list = []

for i in range(n):
    # 먹은 접시
    d_set = set(itertools.islice(queue, k))

    if c not in d_set:
        ans_list.append(len(d_set)+1)
    else:
        ans_list.append(len(d_set))

    queue.rotate(-1)

print(max(ans_list))