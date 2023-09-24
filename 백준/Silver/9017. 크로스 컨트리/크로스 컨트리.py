import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    n_list = list(map(int, input().split()))

    n_dict = dict()

    for i in n_list:
        if i not in n_dict:
            n_dict[i] = 1
        else:
            n_dict[i] += 1

    # 6 미만 인 팀
    n_checkTeam = []
    for k, v in n_dict.items():
        if v < 6:
            n_checkTeam.append(k)

    cnt = 1

    n_team = [0 for i in range(len(n_dict)+1)]
    n_teamCheckNum = [0 for i in range(len(n_dict)+1)]
    n_teamCheckFirst = [0 for i in range(len(n_dict)+1)]

    for i in range(n):
        n_teamCheckNum[n_list[i]] += 1

        # 처음으로 팀의 5번째 주자가 통과했을 떄 ( 동점 주자 체크 )
        if n_teamCheckNum[n_list[i]] == 5:
            n_teamCheckFirst[n_list[i]] = cnt

        if n_list[i] in n_checkTeam:
            continue

        if n_teamCheckNum[n_list[i]] > 4:
            cnt += 1
            continue

        n_team[n_list[i]] += cnt
        cnt += 1

    # 정답 인덱스, 숫자
    ansIndex, ansNum = 0, 1000000000

    for i in range(1, len(n_dict)+1):
        if n_team[i] == 0:
            continue

        if n_team[i] < ansNum:
            ansNum = n_team[i]
            ansIndex = i
        # 5번째 주자 비교
        if n_team[i] == ansNum:
            if n_teamCheckFirst[i] < n_teamCheckFirst[ansIndex]:
                ansIndex = i

    print(ansIndex)