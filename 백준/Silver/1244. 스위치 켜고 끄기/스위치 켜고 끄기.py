import sys

input = sys.stdin.readline

sw = int(input())

switches = list(map(int, input().split()))

po = int(input())
people_list = [list(map(int, input().split())) for _ in range(po)]

for i in people_list:
    # x : 성별, y : 스위치 번호
    x, y = i

    # 남자일 때
    if x == 1:
        for jump in range(y-1, sw, y):
            if switches[jump] == 1:
                switches[jump] = 0
            else:
                switches[jump] = 1
    # 여자일 때
    elif x == 2:
        # index 맞추기
        y -= 1

        # 현 위치 바꾸기
        if switches[y] == 1:
            switches[y] = 0
        else:
            switches[y] = 1

        # 좌우 비교하기
        y1, y2 = y-1, y+1

        while y1 >= 0 and y2 < sw:
            if switches[y1] == switches[y2]:
                if switches[y1] == 1:
                    switches[y1], switches[y2] = 0, 0
                else:
                    switches[y1], switches[y2] = 1, 1
            else:
                break
            y1 -= 1
            y2 += 1

cnt = 0

for i in range(sw):
    print(switches[i], end=' ')

    # 띄어쓰기 할 갯수
    cnt += 1

    if cnt == 20:
        cnt = 0
        print()