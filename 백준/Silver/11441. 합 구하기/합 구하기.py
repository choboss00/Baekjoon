"""
11441번 : 합 구하기 ( 실버 3 )

1. N개의 수 A1 ~ AN 이 입력으로 주어짐
2. 총 M 개의 구간 i, j 가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램 작성하기

풀이
1. 사각형 생각하기
"""
import sys

input = sys.stdin.readline
# 입력값 받기
n = int(input())
n_list = list(map(int, input().split()))

# 입력 리스트의 구간합 구하기
np_list = []
subNum = 0
for i in range(n):
    subNum += n_list[i]
    np_list.append(subNum)
    
# 구간 입력값
m = int(input())
res = []
for _ in range(m):
    a, b = map(int, input().split())

    resNum = 0
    # 값 계산하기
    if a == 1:
        resNum = np_list[b-1]
    else:
        resNum = np_list[b-1] - np_list[a-2]
    res.append(resNum)

for j in res:
    print(j)
