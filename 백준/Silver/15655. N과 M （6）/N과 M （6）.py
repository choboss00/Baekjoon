import sys

def back(list, back_list, level, depth):
    if len(back_list) == m:
        print(*back_list)
        return

    for i in range(level, depth):
        back_list.append(list[i])
        back(list, back_list, i+1, depth)
        back_list.pop()

input = sys.stdin.readline

n, m = map(int, input().split())
n_list = list(map(int, input().split()))

n_list.sort() # 오름차순 정렬
back_list = [] # 백트래킹 원소를 저장할 리스트
# back : list, back_list, level, depth
back(n_list, back_list, 0, n)