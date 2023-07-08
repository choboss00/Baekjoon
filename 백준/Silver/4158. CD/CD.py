"""
4158번. CD ( 실버 5 )
"""
import sys

input = sys.stdin.readline

n,m = 1,1

while n != 0 and m != 0:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    n_d = dict()
    m_d = dict()
    for i in range(n):
       n_d[input().strip()] = 1
    for i in range(m):
       m_d[input().strip()] = 1

    cnt = 0
    for k1,v1 in n_d.items():
        if k1 in m_d:
            cnt += 1
    print(cnt)