import sys
from collections import deque
# N개의 리스트 받기
N = int(sys.stdin.readline().strip())
N_list = []
# N개의 중요도 받기
M_list = []
num = 0
for i in range(N):
    N_list.append(sys.stdin.readline().split())
    M_list.append(sys.stdin.readline().split())
    # 1 ~ 리스트 숫자까지 리스트 생성
    new_list = list(j for j in range(1, int(N_list[num][0]) + 1))
    # 내가 바꿔야할 위치의 인덱스값 받아오기
    Inx = new_list.index(int(N_list[num][0]))
    # 자리 바꾸기
    tmp = new_list[Inx] # 원래 4번 값
    new_list[Inx] = new_list[int(N_list[num][1])] # 원래 4번의 위치에 다른 값 넣기
    new_list[int(N_list[num][1])] = tmp # 4번 값을 내가 설정해준 위치에 넣기

    # 중요도 부여
    dic = {}
    k = 0
    for j in new_list:
        dic[j] = int(M_list[i][k])
        k += 1
    # 값 출력 기준 1. 중요도 2. 숫자가 작은 순서부터
    dic_list = deque(dic.items())
    count = 1
    l = 0
    while(len(dic_list) != 0):
        max_list = []
        for i in range(len(dic_list)):
            # max값 구하기
            max_list.append(dic_list[i][1])
        Max = max(max_list)

        if(dic_list[l][1] == Max):
            if(int(N_list[num][0]) == dic_list[l][0]):
                print(count)
                break
            else:
                dic_list.popleft()
                count += 1
        else:
            dic_list.append(dic_list[l])
            del dic_list[l]
    # 다음 리스트 확인
    num += 1
    if(num > N):
        break