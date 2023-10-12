import sys
import heapq

input = sys.stdin.readline

n = int(input())
n_list = []
heap = []

for _ in range(n):
    n_list.append(list(map(int, input().split())))

n_list.sort(key=lambda x: (x[1],x[2]))

# 강의실 갯수
cnt = 0

for idx, ft1, lt1 in n_list:

    if len(heap) == 0:
        # 강의실 추가
        heapq.heappush(heap, lt1)
        cnt += 1
        continue

    lt2 = heapq.heappop(heap)

    # 현재 끝난 시간과 다음 수업의 시작 시간 비교
    if lt2 <= ft1:
        heapq.heappush(heap, lt1)
    else:
        heapq.heappush(heap, lt2)
        heapq.heappush(heap, lt1)
        cnt += 1

print(cnt)