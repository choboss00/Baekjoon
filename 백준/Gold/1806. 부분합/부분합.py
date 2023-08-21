import sys

input = sys.stdin.readline

n,s = map(int, input().split())
n_list = list(map(int, input().split())) + [0]

start, end = 0, 0
length = 0
# 부분 합
sumNum = 0
# 정답
ans = 100000001
# 리스트의 끝까지 탐색 진행
while end <= n:
    # s 값에 못 미칠 경우
    if sumNum < s:
        sumNum += n_list[end]
        # 그 다음으로 이동
        length += 1
        end += 1
    else:
        ans = min(ans, length)
        # 왼쪽 한칸 이동
        start += 1
        # 왼쪽으로 한칸 이동했으니 이전값 빼기
        sumNum -= n_list[start-1]
        length -= 1

if ans == 100000001:
    print(0)
else:
    print(ans)