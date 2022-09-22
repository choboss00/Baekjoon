import sys
# N 값과 N개의 리스트 받기
N = int(sys.stdin.readline().strip())
N_list = list(map(int, sys.stdin.readline().split()))
# M 값과 M개의 리스트 받기
M = int(sys.stdin.readline().strip())
M_list = list(map(int, sys.stdin.readline().split()))

# M개의 리스트에 적혀있는 숫자가 N개의 리스트에 몇개 존재하는지 출력하는 프로그램 작성

dic = {}
# 딕셔너리로 N 개의 리스트 중복값 계산해서 key, value 값으로 나타내기
for i in N_list:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1


# M 리스트 값과 딕셔너리 값 비교후, 존재하면 딕셔너리의 value 값 출력, 없으면 0 출력
for i in M_list:
    if (i in dic.keys()):
        print(dic[i], end=' ')
    else:
        print(0, end=' ')
