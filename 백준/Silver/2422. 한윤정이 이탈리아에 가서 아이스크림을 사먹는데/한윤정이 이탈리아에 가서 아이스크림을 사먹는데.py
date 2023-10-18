"""
백준 2422번 : 한윤정이 이탈리아에 가서 아이스크림을 사먹는데

1. n 종류의 아이스크림

2. 어떤 종류의 아이스크림을 함께 먹으면, 맛이 없어짐

3. 이런 경우를 피하면서 3가지의 아이스크림 선택

4. 이때 선택하는 방법이 몇 가지 인지 구하기

입력
1. 정수 n, m
- n : 아이스크림 종류의 수
- m : 섞어먹으면 안되는 조합의 갯수

출력
1. 가능한 방법이 총 몇 개 있는지 출력하기
"""
import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())

ans = 0
visited = [[False] * (n) for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())

    visited[a-1][b-1] = True
    visited[b-1][a-1] = True


ans = 0

for i in combinations(range(n), 3):
    if visited[i[0]][i[1]] or visited[i[0]][i[2]] or visited[i[1]][i[2]]:
        continue

    ans += 1

print(ans)

