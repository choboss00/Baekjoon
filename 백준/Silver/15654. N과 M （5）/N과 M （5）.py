import sys
def back():
    if len(ans_list) == m:
        print(*ans_list)
        return

    for i in n_list:
        if i in ans_list:
            continue
        ans_list.append(i)
        back()
        ans_list.pop()



input = sys.stdin.readline

n,m = map(int, input().split())
n_list = list(map(int, input().split()))

# 정렬
n_list.sort()

ans_list = []
back()