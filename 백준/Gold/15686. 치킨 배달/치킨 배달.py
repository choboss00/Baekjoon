"""
15686번 : 치킨 배달
1. 크기 : n * n 인 도시가 있음
- 도시 : 1 * 1 크기
- 도시의 각 칸 : 빈칸, 치킨집, 집 3개중 하나
2. 치킨 거리 : 집과 가장 가까운 치킨집 사이의 거리
- 치킨 거리 : 집을 기준으로 정해짐
- 도시의 치킨 거리 : 모든 집의 치킨 거리의 합
3. 도시에 있는 치킨집 중 최대 M 개를 고르고, 나머지는 고르면 안됨
- 어떻게 골라야 도시의 치킨 거리가 가장 작게 될지 구하기

입력
1. N, M
2. N 개의 줄 : 도시의 정보
3. 도시의 정보 : 0, 1, 2
- 0 : 빈칸, 1 : 집, 2 : 치킨집
4. 집의 개수 < 2N, 적어도 1개는 존재함
5. M <= 치킨집의 갯수 <= 13

출력
1. 첫째 줄에 폐업시키지 않을 치킨집 M 개를 골랐을 때, 도시의 치킨거리 최솟값 구하기

풀이
1. 조합 + 거리 계산
2. M 개의 치킨집을 고른 뒤, 각 1의 위치마다 거리 계산해서 최솟값 찾기
"""
import sys
from itertools import combinations

input = sys.stdin.readline

# 입력값 받기
n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

chicken_list = []
home_list = []

for y in range(n):
    for x in range(n):
        if maps[y][x] == 1:
            home_list.append([x,y]) # 집
        elif maps[y][x] == 2:
            chicken_list.append([x,y]) # 치킨집

chicken_coms = list(combinations(chicken_list, m)) # 조합

ans_list = []

for chicken_sub_list in chicken_coms:
    sub_list = []
    for chicken_home in chicken_sub_list:
        x0 = chicken_home[0]
        y0 = chicken_home[1]
        sub_list2 = []
        for home in home_list:
            x1 = home[0]
            y1=  home[1]
            sub_list2.append(abs(x0-x1) + abs(y0-y1))
        sub_list.append(sub_list2)

    final_list = []

    for x in range(len(sub_list[0])):
        num = 9999
        for y in range(len(sub_list)):
            if sub_list[y][x] < num:
                num = sub_list[y][x]
        final_list.append(num)

    ans_list.append(sum(final_list))

print(min(ans_list))


