import sys
# 숫자 넣기
N, M = map(int, sys.stdin.readline().split())
# 리스트에 문자 넣기
N_lst = list(sys.stdin.readline().strip() for i in range(N))
M_lst = list(sys.stdin.readline().strip() for i in range(M))
# 리스트 사전순 정렬
N_dict = {}
for i in range(N):
    N_dict[N_lst[i]] = i
# 리스트가 같으면 +1, 문자열 가져오기. 리스트 첫번재 문자끼리 비교 후, 다르면 바로 break
cnt = 0
cnt_lst = []
for i in range(len(M_lst)):
    if M_lst[i] in N_dict:
        cnt += 1
        cnt_lst.append(M_lst[i])

cnt_lst = sorted(cnt_lst)
# 출력
print(cnt)
for i in cnt_lst:
    print(i)