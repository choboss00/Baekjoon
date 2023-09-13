import sys

def back(lst, level, depth):
    if len(back_list) == 6:
        print(*back_list)
        return

    for i in range(level, depth):
        back_list.append(lst[i])
        back(lst, i+1, depth)
        back_list.pop()

input = sys.stdin.readline

while True:
    n_list = list(map(int, input().split()))

    # 만약 0이 들어왔을 경우 종료
    if n_list.pop(0) == 0:
        break

    # 6개의 수를 선택해서 차례대로 출력 ( 사전순 )
    n_list.sort()

    # 백트래킹을 돌며 원소를 출력할 리스트
    back_list = []

    back(n_list, 0, len(n_list))

    print()