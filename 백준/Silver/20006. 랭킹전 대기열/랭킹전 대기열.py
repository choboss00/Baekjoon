import sys

input = sys.stdin.readline

# 플레이어의 수 p, 방의 정원 m
p, m = map(int, input().split())

# 방
rooms = []
# 플레이어의 수 만큼 반복
for i in range(p):
    # 방에 들어갔는지 체크
    check = False
    # 첫번째 플레이어
    l, n = input().split()
    if i == 0:
        rooms.append([(int(l), n)])
    else:
        # room 을 차례대로 돌면서 가장 첫번째 값과 비교하기
        for j in range(len(rooms)):
            # 아직 정원이 덜 찬경우
            if len(rooms[j]) < m:
                if rooms[j][0][0] - 10 <= int(l) <= rooms[j][0][0] + 10:
                    rooms[j].append((int(l), n))
                    check = True
                    break
            # 방을 다 돌았는데도 들어갈 수 있는 방이 없을 경우 새로운 방 만들기
            elif j == len(rooms)-1:
                rooms.append([(int(l), n)])
                check = True
                break
        # 들어갈 수 있는 방이 없는 경우 새로운 방 만들기
        if check == False:
            rooms.append([(int(l), n)])

for room in rooms:
    room.sort(key=lambda x : x[1])

    # 방이 다 찬 경우
    if len(room) == m:
        print("Started!")
        for r in room:
            print(*r)
    else:
        print("Waiting!")
        for r in room:
            print(*r)