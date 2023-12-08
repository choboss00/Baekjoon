import sys

input = sys.stdin.readline

tri = [(i*(i+1)) // 2 for i in range(45)]

check = [0] * 1001

for i in range(1, 45):
    for j in range(i, 45):
        for k in range(j, 45):
            now = tri[i] + tri[j] + tri[k]

            if now <= 1000:
                check[now] = 1

t = int(input())

for _ in range(t):
    K = int(input())
    print(check[K])

