import sys
import bisect

input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))

dp = [n_list[0]]
len_list = [(n_list[0], 0)]

for i in range(1, n):
    target = n_list[i]

    # 끝값과 비교
    if dp[-1] < target:
        dp.append(target)
        len_list.append((target, len(dp)-1))
    else:
        idx = bisect.bisect_left(dp, target)
        dp[idx] = target
        len_list.append((target, idx))

res = []
# 체크해야할 리스트의 길이
check = len(dp)-1

for i in range(len(len_list)-1, -1, -1):

    if len_list[i][1] == check:
        res.append(len_list[i][0])
        check -= 1

print(len(res))
print(*reversed(res))