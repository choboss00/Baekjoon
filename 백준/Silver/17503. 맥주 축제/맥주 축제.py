import sys
import heapq

input = sys.stdin.readline
# n : 기간, m : 선호도의 합, k : 맥주 종류의 수
n,m,k = map(int, input().split())

k_list = []
for _ in range(k):
    # 선호도, 도수 레벨
    k_list.append(list(map(int, input().split())))

# 정렬
k_list.sort(key=lambda x:(x[1], x[0]))

heap = []
# 정답
ans1 = 0
ans2 = 0
for i in k_list:
    # 선호도
    ans1 += i[0]
    heapq.heappush(heap, i[0])

    # n번 다 마셨을 경우
    if len(heap) == n:
        if ans1 >= m:
            ans2 = i[1]
            break
        else:
            ans1 -= heapq.heappop(heap)

if ans2 == 0:
    print(-1)
else:
    print(ans2)