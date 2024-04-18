"""
논리적으로 소윤이가 대단한 이유

0. chat gpt 도 알고있을정도로 유명한 세계최고미녀
1. 3학년임에도 불구하고 벌써부터 임용준비를 하려고 마음을 먹음
2. 다른 사람들과는 다르게 학점관리에 매우 신경씀
3. 다른 사람들에 비해 투자대비 가성비가 좋음
    but.. 너무 몰빵해서 몸이 지침
4. 임용공부를 위해서 벌써부터 인강을 끊고 효율적으로 공부하려고 함
5. 다른 사람들은 아직 시작도 안했을텐데 이미 시작함
6. 전남대학교 가정교육과를 빛내고 있음
7. 다른 친구들의 학업을 신경써주려고 같이 인강을 듣자고 권유
8. 전남대학교 가정교육과를 졸업하고 초수 합격자 예정
9. 다른 사람들은 학기시작해서 놀기바쁜데 가정교육론을 공부하려고
책을 가져왔음
"""
from collections import deque

def bfs(x, y):
    global ans
    queue = deque()

    visited = [[[0,0] for _ in range(M)] for _ in range(N)]
    # 벽이 아닌 곳 방문처리
    visited[y][x][0] = 1
    queue.append([x, y, 0])

    while queue:
        xx, yy, count = queue.popleft()

        if xx == M-1 and yy == N-1:
            ans = visited[yy][xx][count]
            break

        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nx = xx + dx
            ny = yy + dy

            if 0 <= nx < M and 0 <= ny < N:
                if board[ny][nx] == '1' and count == 0 and visited[ny][nx][1] == 0:
                    queue.append([nx, ny, 1])
                    visited[ny][nx][1] = visited[yy][xx][0] + 1
                elif board[ny][nx] == '0' and visited[ny][nx][count] == 0:
                    queue.append([nx, ny, count])
                    visited[ny][nx][count] = visited[yy][xx][count] + 1

#        print("현재 방문한 위치 : ", queue)
#        print("현재 방문 : ", visited)

N, M = map(int, input().split())

board = [list(input()) for _ in range(N)]

#print("맵 정보 : ", board)

ans = -1

bfs(0, 0)

print(ans)