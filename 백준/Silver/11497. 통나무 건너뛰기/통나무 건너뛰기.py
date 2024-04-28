T = int(input())

for _ in range(T):
    N = int(input())
    Ls = list(map(int, input().split()))
    # 정렬
    Ls.sort()

    #print(f"정렬 후 리스트 : {Ls}")

    new_L = [-1 for _ in range(N)]

    count = 0
    left_idx = 0
    right_idx = -1

    for i in Ls:
        if count == 0:
            new_L[left_idx] = i
            left_idx += 1
        else:
            new_L[right_idx] = i
            right_idx -= 1

        count = (count + 1) % 2

    # 최소 난이도 측정하기
    min_level = -1
    for i in range(N):
        if abs(new_L[i-1] - new_L[i]) >= min_level:
            min_level = abs(new_L[i-1] - new_L[i])

    print(min_level)