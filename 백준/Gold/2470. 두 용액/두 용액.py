import sys

input = sys.stdin.readline

n = int(input())

n_list = list(map(int, input().split()))

n_list.sort()

left, right = 0, len(n_list)-1
mm = 2000000001
ans = [n_list[left], n_list[right]]

while left < right:
    tmp = n_list[left]+n_list[right]

    if abs(tmp) < abs(mm):
        ans[0] = n_list[left]
        ans[1] = n_list[right]
        mm = tmp

    if tmp < 0:
        left += 1
    elif tmp > 0:
        right -= 1
    else:
        break

print(*ans)