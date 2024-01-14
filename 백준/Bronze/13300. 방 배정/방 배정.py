"""
## 방 배정

## 문제
1. 학생들이 묵을 방 정하기
- 남자는 남자끼리, 여자는 여자끼리
- 한 방에는 같은 학년의 학생들을 배정해야 함 ( 한 방에 한 명만 배정하는 것도 가능 )

## 입력
1. 학생 수 N, 한 방에 배정가능한 최대 인원 수 K

2. N 개의 줄에는 성별 S, 학년 Y 가 공백으로 분리되어 주어짐
- 0 : 여학생, 1 : 남학생

## 출력
1. 학생들을 모두 배정하기 위해 필요한 최소한의 방 개수 출력하기

## 풀이
1. 여학생, 남학생 나누기

2. 학년별로 나누기
"""
import sys
import math

input = sys.stdin.readline

N, K = map(int, input().split())

girls = [[] for _ in range(6)]
mans = [[] for _ in range(6)]


for _ in range(N):
    s, y = map(int, input().split())

    if s == 0:
        girls[y-1].append(y)
    else:
        mans[y-1].append(y)

ans = 0

for girl in girls:
    if len(girl) == 0: # 비어있음
        continue
    elif len(girl) <= K:
        ans += 1
    else:
        ans += math.ceil(len(girl) / K)

for man in mans:
    if len(man) == 0:
        continue
    elif len(man) <= K:
        ans += 1
    else:
        ans += math.ceil(len(man) / K)

print(ans)