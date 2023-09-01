
import sys
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())

heap = [] # 보석 ( 무게, 금액 )
bags = [] # 가방
# 보석 넣기
for _ in range(n):
    m, v = map(int, input().split())
    heap.append((m, v))
# 가방 넣기
for _ in range(k):
    bags.append(int(input()))

# 정렬
heap.sort()
bags.sort()

ans = 0
subHeap = []

for bag in bags:
    # 힙에서 가장 큰 순서대로 정렬하기
    while heap and heap[0][0] <= bag:
        heapq.heappush(subHeap, -heap[0][1])
        heapq.heappop(heap)

    # 값이 존재할 경우
    if subHeap:
        ans -= heapq.heappop(subHeap)
print(ans)