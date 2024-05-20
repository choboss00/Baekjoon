# 감소하는 수
N = int(input())

nums = [str(i) for i in range(10)]

cnt = 1

while cnt < 10:
    for n in nums:
        if len(n) == cnt: # 자릿수 체크
            for j in range(10):
                if int(n[-1]) > j:
                    nums.append(n + str(j))
    cnt += 1

if N > 1022:
    print(-1)
else:
    print(nums[N])