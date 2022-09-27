import sys
# 수행할 연산의 수 M 받기
M = int(sys.stdin.readline().strip())
# 집합 s
s = set()
# 연산 수행 프로그램 작성
for i in range(M):
    M_lst = sys.stdin.readline().split()
    if(len(M_lst) == 1):
        if (M_lst[0] == "all"):
            s = set([i for i in range(1, 21)])
        else:
            s = set()
        continue
    # add
    if(M_lst[0] == "add"):
        s.add(int(M_lst[1]))
    # remove
    if(M_lst[0] == "remove"):
        s.discard(int(M_lst[1]))
    # check
    if(M_lst[0] == "check"):
        if int(M_lst[1]) in s:
            print(1)
        else:
            print(0)
    # toggle
    if(M_lst[0] == "toggle"):
        if int(M_lst[1]) in s:
            s.discard(int(M_lst[1]))
        else:
            s.add(int(M_lst[1]))