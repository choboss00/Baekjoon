"""
1459번. 걷기

1. 도시의 크기 : 무한대
2. 세준이의 현재 위치 : ( 0, 0 )
- (X, Y) 에 위치한 집으로 가려고 함
3. 세준이가 걸을 수 있는 방법 : 2가지
- 도로를 따라서 가로, 세로로 한 블록 움직이기 (0, 1), (1, 0)
- 블록은 대각선으로 가로지르기 (1, 1)
4. 세준이가 집으로 가는데 걸리는 최소 시간 구하기

풀이
1. 가로 + 세로 이동값과 대각선 이동값 비교
2. 더 저렴한 방식으로 이동하기

"""
import sys

input = sys.stdin.readline

# x, y : 집의 위치
# w : 직선 이동, s : 대각선 이동
x, y, w, s = map(int, input().split())

# 최소 비용
ans = 0

# 현재 위치
now_x, now_y = 0, 0

# 대각선 이동이 가능할 경우
min_xy = min(x, y)

x -= min_xy
y -= min_xy

cost = 0

if w * 2 < s:
    cost = w * 2
else:
    cost = s

ans += min_xy * cost

# 한쪽 방향 이동 ( 남아있는 수 : 짝수 / 홀수 생각해줘야 함 )
if w < s:
    cost = w
else:
    cost = s
# 남아있는 수가 짝수 일 경우
if max(x, y) % 2 == 0:
    ans += max(x, y) * cost
else:
    if w < s:
        ans += max(x, y) * cost
    else:
        ans += max(x, y) * cost + (w - s)

print(ans)