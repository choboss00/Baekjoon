import sys

N = list(sys.stdin.readline().split())

M = [0 for i in range(len(N))]

for i in range(len(N)):
    M[i] = int(N[i][::-1])

print(max(M))