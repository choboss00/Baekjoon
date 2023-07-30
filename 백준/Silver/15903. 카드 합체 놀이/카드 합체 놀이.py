import sys
import heapq

input = sys.stdin.readline

n,m = map(int, input().split())
# 리스트 생성
heap = list(map(int,input().split()))

# 힙 변환
heapq.heapify(heap)

for _ in range(m):
    num1, num2 = heapq.heappop(heap), heapq.heappop(heap)

    ans = num1+num2

    for i in range(2):
        heapq.heappush(heap, ans)

print(sum(heap))