"""
15903번. 카드 합체 놀이

자연수가 쓰여진 카드 n장

1. x 번 카드와 y 번 카드를 골라 그 두장에 쓰여진 수를 더한 값 계산
-> x, y 카드 다름

2. 계산한 값을 x번 카드와 y번 카드 두장 모두에 덮어 쓴다

이걸 m 번 진행
-> n 장의 카드에 쓰여있는 수를 모두 더한 값이 최종 값
-> 이 최종 값을 가장 작게 만드는 것이 목표

만들 수 있는 가장 작은 점수 계산 프로그램 만들기

입력
카드의 개수 : n
카드 합체 횟수 : m

최소 힙
-> 2개 빼서 더하고
-> 다시 힙정렬

"""
import sys
import heapq

input = sys.stdin.readline

n,m = map(int, input().split())
# 리스트 생성
n_list = list(map(int,input().split()))

heap = []
# 최소 힙 공간에 넣기
for i in n_list:
    heapq.heappush(heap, i)
# m 이 양수일 때 반복
while m > 0:
    num1 = heapq.heappop(heap)
    num2 = heapq.heappop(heap)

    ans = num1+num2
    # 넣기
    for i in range(2):
        heapq.heappush(heap, ans)

    # 횟수 감소
    m -= 1

print(sum(heap))
