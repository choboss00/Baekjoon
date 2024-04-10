import sys

input = sys.stdin.readline

N, M, R = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(N)]

for _ in range(R):
    for i in range(min(N, M) // 2):
        x, y = i, i

        temp = data[y][x]

        # 왼쪽
        for j in range(i+1, N-i):
            y = j
            prev_data = data[y][x]
            data[y][x] = temp
            temp = prev_data

        # 아래
        for k in range(i+1, M-i):
            x = k
            prev_data = data[y][x]
            data[y][x] = temp
            temp = prev_data

        # 오른쪽
        for l in range(i+1, N-i):
            y = N-l-1
            prev_data = data[y][x]
            data[y][x] = temp
            temp = prev_data

        # 위
        for m in range(i+1, M-i):
            x = M-m-1
            prev_data = data[y][x]
            data[y][x] = temp
            temp = prev_data

for y in range(N):
    for x in range(M):
        print(data[y][x], end=' ')
    print()
