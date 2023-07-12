"""
16212번. 정열적인 정렬
"""

n = int(input())
l = list(map(int, input().split()))
l.sort()

for i in l:
    print(i, end=' ')