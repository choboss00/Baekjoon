"""
26069번. 붙임성 좋은 총총이 ( 실버 4 )

댄스 -> 한번 본 사람은 따라함

사람들의 만난 기록 : n
댄스를 추지 않던 사람이 사람을 만나면 댄스를 추게 됨
총총이만 처음에 출 때, 마지막 기록 이후 몇명이 추는지 구하기

"""
import sys

input = sys.stdin.readline

n = int(input())

d = dict()

for i in range(n):
    a,b = input().split()
    # 이름이 없는 경우
    if a not in d:
        d[a] = 0
    if b not in d:
        d[b] = 0
    # 만난 경우
    if a == 'ChongChong':
        d[b] += 1
    elif b == 'ChongChong':
        d[a] += 1
    elif d[a] != 0:
        d[b] += 1
    elif d[b] != 0:
        d[a] += 1
ans = 1
for k,v in d.items():
    if v != 0:
        ans += 1
print(ans)