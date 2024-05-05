N, L = map(int, input().split())

n_list = [list(map(int, input().split())) for _ in range(N)]

# 정렬
n_list.sort()

# 널빤지 수
ans = 0

for i in range(N):
    length = n_list[i][1] - n_list[i][0]

    # 마지막 웅덩이
    if i == N-1:
        ans += ((length-1) // L + 1)
        break
    # 길이가 나누어떨어지지 않을 경우
    if length % L:
        # 널빤지의 남은 부분
        temp_length = L - (length % L)
        # 다음 길이 비교해야 함
        _next = n_list[i][1] + temp_length

        if _next >= n_list[i+1][0]:
            n_list[i+1][0] = _next

        # 더해주기
        ans += (length // L + 1)
    else:
        ans += length // L

print(ans)


