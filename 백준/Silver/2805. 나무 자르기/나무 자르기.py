import sys

input = sys.stdin.readline

n,m = map(int, input().split())

n_list = list(map(int, input().split()))

left, right = 1, max(n_list)
# 결과를 담는 변수
res = 0
while left <= right:
    mid = (left+right)//2
    num = 0
    for i in range(n):
        # 현재 절단기 값보다 작을경우
        if mid > n_list[i]:
            continue
        num += (n_list[i]-mid)

    # 만약 현재 나무토막 크기가 더 클 경우
    if num >= m:
        left = mid+1
        res = mid
    else:
        right = mid-1

print(res)