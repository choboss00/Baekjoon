"""

## 숫자고르기

## 문제
1. 세로 2줄, 가로로 N개의 칸으로 이루어진 표

2. 둘째 줄의 각 칸에는 1 이상, N 이하인 정수가 들어있음

3. 첫째 줄에서 숫자를 적절히 뽑으면, 그 뽑힌 정수들이 이루는 집합과, 뽑힙 정수들의 바로 밑의 둘째 줄에 들어있는 정수들의 집합이 일치함

4. 이러한 조건을 만족시키도록 정수를 뽑되, 최대로 많이 뽑는 방법을 찾는 프로그램 작성하기

## 입력
1. N

2. 표의 두번째 줄에 들어가는 정수들이 순서대로 한 줄에 하나씩 입력됨

## 출력
1. 뽑힌 정수들의 개수 출력

2. 뽑힌 정수들을 작은 수부터 큰 수의 순서로 한 줄에 하나씩 출력

## 풀이
1. 딕셔너리

"""
import sys

input = sys.stdin.readline

ans_list = []

def dfs(idx):
    if not visited[idx]: # 아직 방문하지 않은 경우
        visited[idx] = True
        up.add(idx + 1)
        down.add(n_list[idx])
        if up == down:
            ans_list.extend(list(down))
            return
        dfs(n_list[idx] - 1)

n = int(input())

n_list = []

for i in range(n):
    n_list.append(int(input()))

for i in range(n):
    visited = [False for _ in range(n)]
    up = set()
    down = set()
    dfs(i)

ans_list = list(set(ans_list))
ans_list.sort()

print(len(ans_list))
for a in ans_list:
    print(a)

