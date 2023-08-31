import sys
import heapq

input = sys.stdin.readline

n = int(input())
heap = []
for i in range(n):
    a_list = list(map(int, input().split()))

    # a 가 0 일경우
    if a_list[0] == 0:
        if len(heap) == 0:
            print(-1)
        else:
            print(-heapq.heappop(heap))
    else:
        for j in range(1, len(a_list)):
            heapq.heappush(heap, -a_list[j])