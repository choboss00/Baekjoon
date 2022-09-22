import sys
# N값 받기
N = int(sys.stdin.readline().strip())
# List 정렬
N_list = []
for i in range(N):
    N_list.append(int(sys.stdin.readline().strip()))
N_list.sort()

# 최빈값을 구하기 위해 dictionary 사용
dic = {}

for i in N_list:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
# dictionary value값으로 정렬 그 후 key 값으로 정렬
max_dic = max(dic.values())
dic = sorted(dic.items(), key=lambda x: (x[1], x[0]))

# dictionary 최빈값만 제외하고 삭제
i = 0
while(True):
    if(dic[i][1] != max_dic):
        del dic[i]
    else:
        break

# 산술평균 출력. 소숫점 첫째 자리에서 반올림
sum = round(sum(N_list) / len(N_list))
print(sum)
# 중앙값 출력
print(N_list[int(len(N_list)/2)])
# 최빈값 출력
if(len(dic) == 1):
    print(dic[0][0])
else:
    print(dic[1][0])
# 범위 출력
print(max(N_list) - min(N_list))