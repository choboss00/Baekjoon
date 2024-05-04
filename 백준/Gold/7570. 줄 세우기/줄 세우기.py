N = int(input())
nums = list(map(int, input().split()))
idx = [-1] * (N+1)

for i, v in enumerate(nums):
#    print(f"i, v : ", i, v)
    idx[v] = i

#print(f"현재 각 번호의 위치 : {idx}")

cnt = 1
longest = 0

for i in range(1, N):
    if idx[i] < idx[i+1]:
        cnt += 1
    else:
        longest = max(longest, cnt)
        cnt = 1

print(N-longest if N != 1 else 0)