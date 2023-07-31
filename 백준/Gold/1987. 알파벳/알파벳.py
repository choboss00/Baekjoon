import sys
def back(x,y, cnt):
    global ans
    # 최대 깊이 계산
    ans = max(ans, cnt)
    
    if ans == 26:
        return

    for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
        nx = x + dx
        ny = y + dy

        # 예외 처리
        if 0 <= nx < c and 0 <= ny < r:
            # 아직 방문하지 않았을 경우
            if not visited[board[ny][nx]]:
                # 방문 처리
                visited[board[ny][nx]] = True
                back(nx,ny, cnt + 1)
                visited[board[ny][nx]] = False

input = sys.stdin.readline

r,c = map(int, input().split())
board = [list(map(lambda x: ord(x) - 65, input().strip())) for _ in range(r)]

visited = [False for _ in range(26)]

# 처음 위치 방문 처리
visited[board[0][0]] = True
ans = 1

back(0,0,1)
print(ans)