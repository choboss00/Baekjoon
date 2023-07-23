"""
12018번 : Yonsei TOTO

주어진 마일리지로 최대한 많은 과목 신청
마일리지는 한 과목에 1 ~ 36 까지 넣을 수 있음

첫째 줄 : 과목수 n, 주어진 마일리지 m
둘째줄 : 각 과목에 신청한 사람수 Pi 와 과목의 수강인원 Li
그 다음줄 : 각 사람이 마일리지를 얼마나 넣었는지
마일리지가 같을 경우, 성준이에게 우선순위

1. 마일리지 큰순으로 정렬
2. 과목의 수강인원 마지막 수 만큼 비교
"""
import sys

input = sys.stdin.readline

# 과목수 n, 마일리지 m
n,m = map(int,input().split())

# 리스트
lst = []
# n번 반복
for _ in range(n):
    # 신청 수 p, 수강 인원 l
    p,l = map(int,input().split())
    # 신청 수보다 수강 인원이 널널할경우
    if p < l:
        # 입력값은 받아줘야 함
        p_list = list(map(int, input().split()))
        lst.append(1)
    else:
        # 신청 인원 리스트
        p_list = list(map(int,input().split()))
        # 역순 정렬
        p_list.sort(reverse=True)

        # 수강 인원만큼 자르기
        lst.append(p_list[l-1])

lst.sort()
# 갯수
cnt = 0

for i in lst:
    if m >= i:
        m -= i
        cnt += 1
print(cnt)