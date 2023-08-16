from collections import deque
    
def solution(maps):
    # n, m
    n = len(maps[0])
    m = len(maps)
    
    # 갈 수 있는 경우
    queue = deque()
    
    queue.append((0,0))
    
    while queue:
        x,y = queue.popleft()
        
        for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
            nx = x + dx
            ny = y + dy
            
            if 0 <= nx < n and 0 <= ny < m:
                if maps[ny][nx] == 1:
                    queue.append((nx,ny))
                    maps[ny][nx] = maps[y][x] + 1
    
    if maps[m-1][n-1] == 1:
        return -1
    else:
        return maps[m-1][n-1]          
    

"""
map : 5 * 5

처음 위치 : (1,1)
상대 위치 : (5,5)

검정 : 벽 (0)
흰색 : 길 (1)

이동 : 동,서,남,북

가장 빨리 상대 팀 진역으로 가는 방법 찾기
도착할 수 없을 경우, -1 리턴하기

그래프문제 -> bfs 탐색 진행
"""