import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    # n : team, k : problem, t : team id, m : log entry
    n, k, t, m = map(int, input().split())
    # [[0,0,0 ...], [0,0,0 ...] ... ] ( n * k )
    n_list = [[0] * k for _ in range(n)]

    # 제출횟수가 적은 팀
    review_count = [0] * n

    # 빨리 제출한 팀
    fast_count = [0] * n

    # log entry
    for cnt in range(1, m+1):
        # i : team id, j : 문제번호, s : score
        i, j, s = map(int, input().split())
        # max(s, ~)
        n_list[i-1][j-1] = max(n_list[i-1][j-1], s)
        # 제출횟수 체크
        review_count[i-1] += 1
        # 빨리 제출한 순서 체크
        fast_count[i-1] = cnt

    # 점수 합하기
    n_sum_list = [0] * n

    for k in range(n):
        n_sum_list[k] = sum(n_list[k])

    # 등수 구하기
    ans = 1
    # 내 팀의 점수
    my_team_score = n_sum_list[t-1]

    for l in range(n):
        if l == (t-1):
            continue
        if my_team_score < n_sum_list[l]:
            ans += 1
        # 점수가 같을 경우
        elif my_team_score == n_sum_list[l]:
            # 풀이 제출 횟수 비교하기
            # 풀이 횟수가 더 적을경우
            if review_count[t-1] < review_count[l]:
                continue
            elif review_count[t-1] == review_count[l]:
                # 제출 시간 체크
                if fast_count[t-1] < fast_count[l]:
                    continue
                else:
                    ans += 1
            else:
                ans += 1

    print(ans)