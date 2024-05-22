N = int(input())

board = [list(input().strip().split()) for _ in range(N)]

#print(f"초기 복도의 정보 : {board}")

obstacles = []
visited = [[False for _ in range(N)] for _ in range(N)]
# 선생님들의 위치
teachers = []
for y in range(N):
    for x in range(N):
        if board[y][x] == 'T':
            teachers.append((x, y))

#print(f"선생님들의 위치 : {teachers}")
def up(tx, ty):
    while ty > 0:
        ty -= 1
        if board[ty][tx] == 'A':
            return True
        if board[ty][tx] == 'S':
            return False
    return True

def down(tx, ty):
    while ty < N-1:
        ty += 1
        if board[ty][tx] == 'A':
            return True
        if board[ty][tx] == 'S':
            return False
    return True

def left(tx, ty):
    while tx > 0:
        tx -= 1
        if board[ty][tx] == 'A':
            return True
        if board[ty][tx] == 'S':
            return False
    return True

def right(tx, ty):
    while tx < N-1:
        tx += 1
        if board[ty][tx] == 'A':
            return True
        if board[ty][tx] == 'S':
            return False
    return True

def checkTeachers():
    checkStudents = []
    for tx, ty in teachers:
        #print(f"상 : {up(tx, ty)} | 하 : {down(tx, ty)} | 좌 : {left(tx, ty)} | 우 : {right(tx, ty)}")
        if up(tx, ty) and down(tx, ty) and left(tx, ty) and right(tx, ty):
            # 걸린 학생이 아무도 없을 경우
            checkStudents.append(0)
    #print(f"걸린 학생 리스트 : {checkStudents}")
    return checkStudents
def setUpObstacles():
    if len(obstacles) == 3:
        # 선생님들이 학생들을 볼 수 있는지 체크하기
        for ox, oy in obstacles:
            # 장애물 표시하기
            board[oy][ox] = 'A'
        #print(f"장애물 설치 후 : {board}")

        checkTs = checkTeachers()

        if len(checkTs) == len(teachers):
            print("YES")
            exit(0)
        else:
            for ox, oy in obstacles:
                # 원래대로 되돌리기
                board[oy][ox] = 'X'
            return

    for y in range(N):
        for x in range(N):
            if board[y][x] == 'X' and not visited[y][x]:
                obstacles.append((x, y))
                visited[y][x] = True
                setUpObstacles()
                # 이전으로 되돌리기
                obstacles.pop()
                visited[y][x] = False
# 장애물을 놓을 수 있는 장소 구하기
setUpObstacles()
print("NO")