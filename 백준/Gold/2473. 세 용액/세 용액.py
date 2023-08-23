import sys

input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))

# 정렬
n_list.sort()

left, mid, right = 0, (n-1) // 2, n-1

# 정답
ans = [n_list[left], n_list[mid], n_list[right]]

# 임시 합
mm = 4000000001
sumNum = 0

for left in range(0, n-2):
    mid, right = left + 1, n - 1

    while mid < right:
        sumNum = n_list[left] + n_list[mid] + n_list[right]

        if abs(sumNum) < mm:
            mm = abs(sumNum)
            ans[0], ans[1], ans[2] = n_list[left], n_list[mid], n_list[right]

        if sumNum < 0:
            mid += 1
        elif sumNum == 0:
            break
        else:
            right -= 1

print(*ans)