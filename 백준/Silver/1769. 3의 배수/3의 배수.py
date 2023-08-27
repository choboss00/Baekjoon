N = list(input())
ans = 0
cnt = 0
while len(N) != 1:
    ans = sum(map(int, N))
    cnt += 1
    N = list(str(ans))

# 마지막 처리
ans = sum(map(int, N))

print(cnt)

if ans % 3 == 0:
    print('YES')
else:
    print('NO')