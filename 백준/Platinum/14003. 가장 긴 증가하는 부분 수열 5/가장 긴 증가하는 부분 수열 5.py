import sys
import bisect

input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))

ans_list = [n_list[0]]
ans_total = [(n_list[0], 0)]

for i in range(1, n):
    target = n_list[i]

    if ans_list[-1] < target:
        ans_list.append(target)
        ans_total.append((target, len(ans_list)-1))
    else:
        # 이분 탐색
        idx = bisect.bisect_left(ans_list, target)
        ans_list[idx] = target
        ans_total.append((target, idx))

lis_len = len(ans_list)-1
res = []

for i in range(len(ans_total)-1, -1, -1):
    if ans_total[i][1] == lis_len:
        res.append(ans_total[i][0])
        lis_len -= 1

print(len(ans_list))
print(*(reversed(res)))
