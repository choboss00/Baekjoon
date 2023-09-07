import sys
def back(cnt, idx):
    global min_num
    # 스타트팀에 인원수를 다 넣었을 때
    if cnt == n // 2:
        # 만들어둔 맵의 가중치를 더하는 작업
        start_num = 0
        link_num = 0

        # 팀 값 더하기
        for y in range(n):
            for x in range(n):
                if visited[y] and visited[x]:
                    start_num += board[y][x]
                elif not visited[y] and not visited[x]:
                    link_num += board[y][x]
        min_num = min(min_num, abs(start_num - link_num))
        return

    for i in range(idx, n):
        # 아직 방문하지 않았을 경우
        if not visited[i]:
            if cnt <= n // 2:
                # 방문 처리
                visited[i] = True
                back(cnt + 1, i + 1)
                # 방문 해제
                visited[i] = False

input = sys.stdin.readline

n = int(input())
# 맵 만들기
board = []

for _ in range(n):
    board.append(list(map(int, input().split())))

# 방문처리
visited = [False] * n

# 최솟값 설정
min_num = int(1e9)

back(0, 0)

print(min_num)