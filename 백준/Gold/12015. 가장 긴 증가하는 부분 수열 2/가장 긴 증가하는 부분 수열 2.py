import sys
import bisect

input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))

# 큰 값만 넣을 리스트
ans_list=[n_list[0]]

for i in range(1, n):
    target = n_list[i]

    # 리스트 값 비교
    if ans_list[-1] < target:
        ans_list.append(target)
    else:
        # 이분탐색 진행
        idx = bisect.bisect_left(ans_list, target)
        ans_list[idx] = target

print(len(ans_list))