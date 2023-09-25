import sys

input = sys.stdin.readline

# 굴다리 길이
N = int(input())
# 가로등 갯수
M = int(input())
# 가로등의 위치
M_location = list(map(int, input().split()))

# 가로등이 가장 왼쪽, 가운데, 가장 오른쪽을 커버하는지 체크
left, right = 0, N

# 정답
ans = 0

while left <= right:
    visited = [False] * 3
    # 현재 가로등의 높이
    h = (left + right) // 2

    # 만약 가로등이 하나뿐일 경우
    if M == 1 and M_location[0] - h <= 0 and M_location[0] + h >= N:
        ans = h
        break

    # 길의 가운데 부분을 커버할 수 있는지
    dist = []

    for i in range(M):
        # 가장 왼쪽의 가로등
        if i == 0:
            if M_location[i] - h <= 0:
                visited[0] = True
            else:
                break

            dist.append(M_location[i] + h)
        # 가장 마지막
        elif i == M-1:
            # 길의 마지막을 비출 수 있어야 함
            if M_location[i] + h >= N:
                visited[2] = True
            else:
                break

            # 가운데를 커버할 수 있는지
            if dist[-1] >= M_location[i] - h:
                visited[1] = True

        else:
            # 두번째 가로등부터 왼쪽 비교, 오른쪽 값 넣기
            if dist[-1] >= M_location[i] - h:
                visited[1] = True
            else:
                visited[1] = False
                break
            # 오른쪽
            dist.append(M_location[i] + h)

    if visited[0] == True and visited[1] == True and visited[2] == True:
        ans = h
        right = (h-1)
    else:
        left = (h+1)

print(ans)