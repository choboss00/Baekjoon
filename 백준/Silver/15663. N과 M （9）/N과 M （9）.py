import sys
def back():
    # 완료 조건
    if len(ans_list) == m:
        print(' '.join(map(str, ans_list)))
        return
    # 중복 숫자를 제거하기 위한 변수
    tmp = 0
    for i in range(n):
        if not visited[i] and tmp != n_list[i]:
            ans_list.append(n_list[i])
            visited[i] = True
            back()
            # 중복 제거
            tmp = n_list[i]
            ans_list.pop()
            visited[i] = False


input = sys.stdin.readline

n,m = map(int, input().split())
n_list = sorted(list(map(int, input().split())))

ans_list = []
# 방문 처리
visited = [False for _ in range(n)]

back()