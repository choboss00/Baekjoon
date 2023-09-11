import sys
def back(start):
    global cnt
    if sum(back_list) == s and len(back_list) > 0:
        cnt += 1

    for i in range(start, n):
        back_list.append(n_list[i])

        back(i + 1)

        back_list.pop()

cnt = 0

input = sys.stdin.readline

n, s = map(int, input().split())
n_list = list(map(int, input().split()))

# 백트래킹 값을 저장할 리스트
back_list = []

back(0)

print(cnt)