import sys

input = sys.stdin.readline

# n : 물품의 수, k : 버틸 수 있는 무게
n, k = map(int, input().split())

# dp
dp = [0 for i in range(k+1)]

# w, v 리스트 만들기
w_list = []
for i in range(n):
    # w : 물건의 무게, v : 물건의 가치
    w, v = map(int, input().split())

    w_list.append([w,v])


for i in range(n):
    for j in range(k, w_list[i][0]-1, -1):
        dp[j] = max(dp[j], dp[j-w_list[i][0]]+w_list[i][1])

print(dp[k])