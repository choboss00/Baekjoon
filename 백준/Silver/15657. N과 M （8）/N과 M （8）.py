import sys

def back():
    if len(ans) == m:
        print(*ans)
        return

    for i in n_list:
        if len(ans) == 0:
            ans.append(i)
            back()
            ans.pop()
        else:
            if ans[-1] <= i:
                ans.append(i)
                back()
                ans.pop()

input = sys.stdin.readline

n,m = map(int, input().split())
n_list = list(map(int, input().split()))

n_list.sort()

ans = []

back()
