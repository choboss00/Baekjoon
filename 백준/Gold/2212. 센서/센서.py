"""
2212번. 센서

n 개의 센서, k 개의 집중국
각 집중국은 센서의 수신 가능 영역 조절 가능
집중국의 수신 가능 영역 : 고속도로 상에서 연결된 구간으로 표현
n개의 센서가 적어도 하나의 집중국과는 통신이 가능해야 함

집중국의 수신 가능 영역의 길이의 합을 최소화해야 함

고속도로 : 직선

각 집중국의 수신 가능 영역의 거리의 합의 초솟값 구하기

집중국의 수신 가능영역의 길이 : 0 이상
모든 센서의 좌표가 다를 필요는 없음 -> 같아도 된다는 뜻

입력

n : 센서의 개수
k : 집중국의 개수
n의 리스트

출력
집중국의 수신 가능 영역의 길이의 합의 최솟값 출력하기

1 3 6 6 7 9

-> 2 3 0 1 2
-> 0 1 2 2 3
문제 풀이
1. 정렬
2. 현 위치와 그 다음 위치간 거리를 저장하는 리스트 만들기


"""

import sys

input = sys.stdin.readline

n = int(input())
k = int(input())
# 기지국이 더 많을 때
if k >= n:
    print(0)
else:
    n_list = list(map(int, input().split()))

    # 리스트 정렬
    n_list.sort()

    # 길이를 저장하는 리스트
    lst = []

    for i in range(len(n_list)-1):
        lst.append(n_list[i+1]-n_list[i])
    # 길이가 많이 차이나는 순으로 정렬
    lst.sort(reverse=True)
    print(sum(lst[k-1:]))


