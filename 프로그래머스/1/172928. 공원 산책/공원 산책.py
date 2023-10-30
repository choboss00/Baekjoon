from collections import deque

def solution(park, routes):
    queue = deque(routes)
    for y in range(len(park)):
        for x in range(len(park[0])):
            if park[y][x] == 'S':
                while queue:
                    route = queue.popleft()
                    direction, value = route.split()
                    value = int(value)
                    
                    for i in range(value):
                        if direction == 'S':
                            y += 1
                            # 이동한 위치에 벽이 있을 경우
                            if y >= len(park) or park[y][x] == 'X':
                                y -= (i+1)
                                break
                        elif direction == 'N':
                            y -= 1
                            # 이동한 위치에 벽이 있을 경우
                            if y < 0 or park[y][x] == 'X':
                                y += (i+1)
                                break
                        elif direction == 'W':
                            x -= 1
                            # 이동한 위치에 벽이 있을 경우
                            if x < 0 or park[y][x] == 'X':
                                x += (i+1)
                                break
                        elif direction == 'E':
                            x += 1
                            # 이동한 위치에 벽이 있을 경우
                            if x >= len(park[0]) or park[y][x] == 'X':
                                x -= (i+1)
                                break

                        
                return y,x

# 지나다니는 길 : O, 장애물 : X, 시작 지점 : S
# 명령에 따라 진행 : 방향 거리
# 명령 수행 전, 공원 벗어나는지 장애물을 만나는지 확인
# 그럴 경우, 해당 명령을 무시하고 다음 명령 수행
# 가로 : W, 세로 : H
# 문자열 배열 ( Board ) : park
# 명령이 담긴 문자열 배열 ( queue ) : routes
# 모든 명령을 수행 후 놓인 위치 [ 세로, 가로 ] return 하기