"""
11060번 : 점프 점프 ( 실버 2 )

문제
1 * N 의 크기 미로

1. 숫자 이하만큼 이동 가능
2. 최소로 오른쪽 끝으로 이동 ( N ) 할 수 있는 횟수 구하기
3. 없으면 -1 출력

"""
import sys

input = sys.stdin.readline

# 입력값 받기
n = int(input())
n_list = list(map(int, input().split()))

d = [1001] * n
d[0] = 0

for i in range(n):
    for j in range(n_list[i]+1):
        if i+j < n and d[i+j] > d[i]+1:
            d[i+j] = d[i]+1

if d[n-1] >= 1001:
    print(-1)
else:
    print(d[n-1])