import sys
import heapq
from collections import deque
# 숫자 N
N = int(sys.stdin.readline().strip())
# 수업 갯수
N_list = []
for i in range(N):
    s, t = map(int, sys.stdin.readline().split())
    N_list.append([s, t])
# 힙에 넣기 전, 시작 시간과 끝나는 시간을 기준으로 정렬
N_list = sorted(N_list, key=lambda x:(x[0], x[1]))
# 리스트 -> 큐
dList = deque(N_list)
# 힙 정렬
hList = []
# 가장 시작 시간이 빠른 강의 중 가장 빠르게 종료하는 강의의 시간 넣기
heapq.heappush(hList, dList.popleft()[1])
# 나머지 강의 처리
while dList:
    # 처음 강의 가져오기
    cnt = dList.popleft()
    # 강의 시간 비교
    fast_T = heapq.heappop(hList)
    if fast_T > cnt[0]:
        heapq.heappush(hList, fast_T)
    heapq.heappush(hList, cnt[1])

print(len(hList))