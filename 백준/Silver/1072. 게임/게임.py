import sys

input = sys.stdin.readline

x, y = map(int, input().split())

# 현재 승률
z = y * 100 // x

# 바뀔 수 없는 승률일 경우
if z >= 99:
    print(-1)
else:
    start = 1
    end = 1000000000
    ans = 0
    while start <= end:
        mid = (start + end) // 2
        # 승률이 z 보다 클 경우
        if (y+mid) * 100 // (x + mid) > z:
            end = mid - 1
            ans = mid
        else:
            start = mid + 1
    print(ans)