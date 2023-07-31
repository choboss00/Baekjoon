import sys

def back(start):
    if len(n_list) == m:
        print(*n_list)
        return

    for i in range(start, n+1):
        n_list.append(i)
        back(i)
        n_list.pop()


input = sys.stdin.readline

n,m = map(int, input().split())

n_list = []

back(1)