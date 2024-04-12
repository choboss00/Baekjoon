from collections import deque
import sys
import copy

input = sys.stdin.readline

N, M, K = map(int, input().split())

# 파이어볼의 정보
fireball_list = deque()

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    # 인덱스 맞추기
    r -= 1
    c -= 1

    fireball_list.append([r, c, m, s, d])

# 방향에 따라 이동
def move_direction_fireball(y, x, fireball):
    ny = (fireball[0] + y) % N
    nx = (fireball[1] + x) % N

    if 0 <= nx < N and 0 <= ny < N:
        fireball[0] = ny
        fireball[1] = nx

# 파이어볼 이동
def move_fireball(fireball):
    d = fireball[-1]
    s = fireball[-2]
    # 위
    if d == 0:
        move_direction_fireball(-s, 0, fireball)
    elif d == 1:
        move_direction_fireball(-s, s, fireball)
    elif d == 2:
        move_direction_fireball(0, s, fireball)
    elif d == 3:
        move_direction_fireball(s, s, fireball)
    elif d == 4:
        move_direction_fireball(s, 0, fireball)
    elif d == 5:
        move_direction_fireball(s, -s, fireball)
    elif d == 6:
        move_direction_fireball(0, -s, fireball)
    elif d == 7:
        move_direction_fireball(-s, -s, fireball)

def select_fireballs():
    d = {}

    for fireball in fireball_list:
        y, x = fireball[0], fireball[1]

        if (y, x) not in d:
            d[(y,x)] = 1
        else:
            d[(y,x)] += 1
    return d

def divide_fireball(d):
    d_keys = d_mass.keys()

    for key in d_keys:
        # 나눠진 질량, 속력 구하기
        smass = d_mass[key] // 5
        # 질량이 0 일 경우, 소멸되어 없어짐
        if smass == 0:
            continue
        # 속력 구하기
        svelocity = d_velocity[key] // d[key]
        # 짝수, 홀수 체크하기 ( False : 짝수, True : 홀수 )
        check = [0, 0]
        # 짝수 체크
        for dr in d_direction[key]:
            if dr % 2 == 0:
                check[0] += 1
            else:
                check[1] += 1
        # 모두 짝수거나 모두 홀수일 경우
        if check[0] == 0 or check[1] == 0:
            for i in range(0, 7, 2):
                fireball_list.append([key[0], key[1], smass, svelocity, i])
        else:
            for i in range(1, 8, 2):
                fireball_list.append([key[0], key[1], smass, svelocity, i])


def remove_fireballs(d):
    global fireball_list
    d_mass = {}
    d_velocity = {}
    d_direction = {}

    new_fireball_list = deque()

    for i in range(len(fireball_list)):
        y, x = fireball_list[i][0], fireball_list[i][1]

        if (y,x) in d and d[(y,x)] >= 2:
            # 질량, 속력, 방향을 누적
            if (y, x) not in d_mass:
                d_mass[(y, x)] = 0
                d_velocity[(y, x)] = 0
                d_direction[(y, x)] = []

            d_mass[(y, x)] += fireball_list[i][2]
            d_velocity[(y, x)] += fireball_list[i][3]
            d_direction[(y, x)].append(fireball_list[i][4])
        else:
            new_fireball_list.append(fireball_list[i])

    fireball_list = copy.deepcopy(new_fireball_list)


    return d_mass, d_velocity, d_direction, fireball_list


# 파이어볼 명령
for _ in range(K):
    # 파이어볼 이동 전

    # 파이어볼 이동
    for fireball in fireball_list:
        move_fireball(fireball)

    # 같은 칸에 있는 파이어볼 하나로 합치기
    d = select_fireballs()

    d_mass, d_velocity, d_direction, fireball_list = remove_fireballs(d)

    divide_fireball(d)

ans = 0

for f in fireball_list:
    ans += f[2]

print(ans)