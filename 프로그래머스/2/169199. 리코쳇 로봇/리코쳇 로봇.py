from collections import deque

def solution(board):
    answer = 0
    queue = deque()
    # 방향
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    n = len(board)
    m = len(board[0])
    
    
    # 방문처리
    visited = [[-1 for _ in range(m)] for _ in range(n)]
    
    for y in range(n):
        for x in range(m):
            if board[y][x] == 'R':
                # 초기 위치 구하기
                queue.append([x,y])
                visited[y][x] = 0
            # 도착지점 설정하기
            if board[y][x] == 'G':
                g_x, g_y = x, y
    
    # bfs 탐색 진행 ( 한 칸씩 가는게 아니라, 벽 or 장애물에 닿을 때 까지 이동 )
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x, y
            # 쭉 미끄러지는 동작
            while True:
                nx += dx[i]
                ny += dy[i]

                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    # 이전으로 돌아가기
                    nx -= dx[i]
                    ny -= dy[i]
                    break

                # 그 다음 위치 체크
                if board[ny][nx] == 'D':          
                    # 이전으로 돌아가기
                    nx -= dx[i]
                    ny -= dy[i]
                    break
            # 예외처리
            if 0 <= nx < m and 0 <= ny < n:
                # 아직 방문하지 않은 경우
                if visited[ny][nx] == -1:
                    queue.append([nx,ny])
                    visited[ny][nx] = visited[y][x] + 1
    
    return visited[g_y][g_x]

"""
1. 리코쳇 로봇
- 격자모양 게임판 위에서 말을 움직이는 게임
- 시작 위치에서 목표 위치까지 최소 몇 번만에 도달할 수 있는지 말하는 게임 ( bfs )
- 상,하,좌,우 4방향
- 장애물, 맨 끝에 부딪힐 때 까지 미끄러져 이동하는 것을 한번의 이동으로 침 ( 한칸 이동이 아님 )
- . : 빈 공간, R : 로봇의 처음 위치, D : 장애물의 위치, G : 목표 지점
2. 포켓몬스터 골드버전 빙판 지형 느낌

풀이
1. 장애물 / 벽을 만날 때 까지 bfs 탐색 진행
2. 적당히 큰 값에 도달했을 때까지 도착하지 못할 경우 -1 리턴
"""