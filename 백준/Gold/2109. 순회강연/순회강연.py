import heapq

n = int(input())
n_list = []

for _ in range(n):
    p, d = map(int, input().split())
    n_list.append([p, d])

n_list.sort(key=lambda x:(x[1], -x[0]))

#print(f"정렬 후 리스트 : {n_list}")

queue = []

for p, d in n_list:
    heapq.heappush(queue, p)

    if len(queue) > d:
        heapq.heappop(queue)
    #print(f"현재 힙 : {queue}")

print(sum(queue))