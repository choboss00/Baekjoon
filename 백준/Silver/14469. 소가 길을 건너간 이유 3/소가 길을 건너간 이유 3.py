"""
14469번. 소가 길을 건너간 이유 3

"""
import sys

input = sys.stdin.readline

n = int(input())
n_list = []

for i in range(n):
    a,b = map(int, input().split())
    n_list.append([a,b])

n_list.sort(key=lambda x:x[0])
# 처음 시작하는 시간 + 끝나는 시간
ans = sum(n_list[0])
# 그 다음 시작하는 시간부터 비교
for i in range(1,n):
    # 그 다음 시작시간과 비교했을 때 더 작을경우
    if ans < n_list[i][0]:
        ans = n_list[i][0]
    ans += n_list[i][1]

print(ans)
