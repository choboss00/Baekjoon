import sys

input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))

left, right = 0, n-1
# 최댓값 설정, 정답
maxNum = 2000000001
ans = [0,0]

while left < right:
    # 비교할 값
    num = n_list[left] + n_list[right]

    if abs(num) < maxNum:
        ans[0], ans[1] = n_list[left], n_list[right]
        maxNum = abs(num)

    if num < 0:
        left += 1
    else:
        right -= 1

print(*ans)