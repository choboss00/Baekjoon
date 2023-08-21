import sys

input = sys.stdin.readline
# 입력값 받기
n = int(input())
n_list = list(map(int, input().split()))

n_list.sort()

cnt = 0
for i in range(n):
    # 투포인터
    left, right = 0, n - 1

    while left < right:
        num = n_list[left] + n_list[right]

        if num == n_list[i]:
            # 다른 수
            if left != i and right != i:
                cnt += 1
                break
            elif left == i:
                left += 1
            else:
                right -= 1
        elif num < n_list[i]:
            left += 1
        else:
            right -= 1

print(cnt)