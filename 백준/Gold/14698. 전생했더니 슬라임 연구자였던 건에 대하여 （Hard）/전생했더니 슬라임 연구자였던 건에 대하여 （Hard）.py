import heapq
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    cs = list(map(int, input().split()))

    queue = []

    for c in cs:
        heapq.heappush(queue, c)

    #print(f"heap : {queue}")

    ans = 1

    while len(queue) > 1:
        num1 = heapq.heappop(queue)
        num2 = heapq.heappop(queue)

        ans = ans * (num1 * num2) % 1000000007

        heapq.heappush(queue, num1 * num2)

    print(ans)
