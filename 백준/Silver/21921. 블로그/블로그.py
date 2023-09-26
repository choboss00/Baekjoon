import sys

input = sys.stdin.readline

n, x = map(int, input().split())

n_list = list(map(int, input().split()))
# 누적합 - 앞부분 값 계산값을 넣을 리스트
x_list = []
# 누적합을 저장할 리스트
prefix_list = [n_list[0]]

for i in range(1, n):
    # 누적합
    prefix_list.append(prefix_list[i-1] + n_list[i])

# 가장 처음 값 넣기
x_list.append(prefix_list[x-1])

# 계산 과정
for j in range(x, n):
    x_list.append(prefix_list[j] - prefix_list[j-x])

# 최댓값을 뽑아내는 과정
ans_list = []
maxNum = max(x_list)

x_list.sort(reverse=True)

for i in x_list:
    if maxNum != i:
        break
    ans_list.append(i)

if maxNum == 0:
    print('SAD')
else:
    print(maxNum)
    print(len(ans_list))