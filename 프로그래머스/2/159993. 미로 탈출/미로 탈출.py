from collections import deque

def solution(maps):
    answer = 0
    
    queue = deque()
    
    n = len(maps)
    m = len(maps[0])
    
    # 방문 처리
    visited = [[-1 for _ in range(m)] for _ in range(n)]
    
    def clearVisited():
        for y in range(n):
            for x in range(m):
                visited[y][x] = -1 # 초기화
    
    # 방향 설정
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for y in range(n):
        for x in range(m):
            # 시작, 도착, 레버 위치 저장하기
            if maps[y][x] == 'S':
                queue.append([x, y])
                visited[y][x] = 0 # 방문처리
            elif maps[y][x] == 'E':
                end_x, end_y = x, y
            elif maps[y][x] == 'L':
                le_x, le_y = x, y
    
    while queue:
        # 현 위치
        x_, y_ = queue.popleft()
        
        for i in range(4):
            # 그 다음 방향
            nx = x_ + dx[i]
            ny = y_ + dy[i]
            
            # 예외 처리
            if 0 <= nx < m and 0 <= ny < n:
                # 아직 방문하지 않았을 경우
                if visited[ny][nx] == -1:
                    # 다음 위치가 레버일 경우
                    if maps[ny][nx] == 'L':
                        # 현 위치를 제외한 나머지 부분 방문처리 초기화
                        sub = visited[y_][x_] + 1
                        clearVisited()
                        queue.clear()
                        queue.append([nx, ny])
                        visited[ny][nx] = sub
                        break
                        
                    # 다음 위치가 도착 지점일 경우
                    if maps[ny][nx] != 'X':
                        queue.append([nx,ny])
                        visited[ny][nx] = visited[y_][x_] + 1
    
    if visited[le_y][le_x] == -1:
        return -1
    else:
        return visited[end_y][end_x]
    

"""
1. 직사각형 격자 형태의 미로 탈출
2. 통로, 벽
- 통로들 중 한 칸에는 미로를 빠져나가는 문이 있음
- 이 문은 레버를 당겨서만 열 수 있음
- 레버 또한 통로들 중 한 칸에 있음
3. 출발 지점 -> 레버가 있는 칸으로 이동 -> 레버 당기고 
-> 미로를 빠져나가는 문이 있는 칸으로 이동
4. 아직 레버를 당기지 않았더라도 출구가 있는 칸을 지나갈 수 있음
5. 미로에서 한 칸을 이동하는데 1초가 걸릴 때 최대한 빨리 미로 탈출하기
- 탈출할 수 없을 경우 -1 return 하기

입출력
1. 5 <= maps <= 100
2. S : 시작 지점, E : 출구 , L : 레버 : O : 통로, X : 벽
- 시작 지점, 출구, 레버는 항상 다른 곳 / 1개씩만 존재함

풀이
1. 출구 위치 저장하기
2. 레버 위치로 도착한 뒤 출구 위치까지 거리 계산 후 return 하기
- 만약 레버의 위치가 -1 일 경우, 레버로 도착할 수 없으니 -1 리턴하기
3. 전체 풀이는 bfs 탐색 진행
"""