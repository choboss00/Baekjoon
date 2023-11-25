from collections import deque

def solution(maps):
    answer = []
    maps2 = []
    
    for sub_map in maps:
        sub = []
        for i in range(len(sub_map)):
            sub.append(sub_map[i])
        maps2.append(sub)
        
    n, m = len(maps2), len(maps2[0])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def bfs(x, y):
        queue = deque()
        
        queue.append([x,y])
        
        cnt = int(maps2[y][x]) # 현재 값
        
        maps2[y][x] = 'X' # 방문처리
        
        while queue:
            x1, y1 = queue.popleft()
            
            for i in range(4):
                nx = x1 + dx[i]
                ny = y1 + dy[i]
                
                if 0 <= nx < m and 0 <= ny < n:
                    if maps2[ny][nx] != 'X':
                        queue.append([nx, ny])
                        cnt += int(maps2[ny][nx])
                        # 방문처리
                        maps2[ny][nx] = 'X'
        return cnt
    
    for y in range(n):
        for x in range(m):
            if maps2[y][x] != 'X': # 식량일 경우
                answer.append(bfs(x, y))
    
    answer.sort()
    
    if len(answer) == 0:
        answer.append(-1)
        return answer
    else:
        return answer
    

"""
1. 여행 지도
- 지도에는 바다와 무인도들에 대한 정보가 표시되어 있음
- 지도 : 1 * 1 크기의 사각형들로 이루어진 직사각형 격자 형태
- 격자의 각 칸에는 'X' 혹은 1 ~ 9 사이의 자연수가 적혀있음
- X : 바다, 숫자 : 무인도
- 상, 하, 좌, 우 로 연결되는 땅들은 하나의 무인도를 이룸
- 숫자 : 식량을 나타냄
- 상, 하, 좌, 우로 연결된 무인도 안에 숫자를 다 합치면 최대 머무를 수 있는 시간
2. 최대 며칠동안 머물 수 있는지 알아본 후 놀러갈 섬 결정하기
3. maps 가 매개변수로 주어질 때, 각 섬에서 최대 며칠씩 머무를 수 있는지 배열에 오름차순으로 return
- 지낼수 있는 무인도가 없다면 -1 return 하기

풀이
1. bfs 탐색으로 섬마다 지낼 수 있는 기간 배열에 담기
"""