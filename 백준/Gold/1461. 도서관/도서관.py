from collections import deque

n, m = map(int, input().split())
book_list = list(map(int, input().split()))

book_list.sort()

plus_queue = deque()
minus_queue = deque()

for b in book_list:
    if b > 0:
        plus_queue.append(b)
    else:
        minus_queue.append(b)

#print(f"양수 큐 : {plus_queue}")
#print(f"음수 큐 : {minus_queue}")

# 음수 최댓값, 양수 최댓값 저장
max_minus, max_plus = -1, -1

if minus_queue:
    max_minus = abs(minus_queue[0])
if plus_queue:
    max_plus = plus_queue[-1]

# M개씩 묶기
plus_list = []
minus_list = []

while plus_queue:
    idx = 0
    sub_plus_list = []
    while idx < m and plus_queue:
        sub_plus_list.append(plus_queue.pop())
        idx += 1
    plus_list.append(sub_plus_list)

while minus_queue:
    idx = 0
    sub_minus_list = []
    while idx < m and minus_queue:
        sub_minus_list.append(minus_queue.popleft())
        idx += 1
    minus_list.append(sub_minus_list)

#print(f"M개로 묶은 양수 리스트 : {plus_list}")
#print(f"M개로 묶은 음수 리스트 : {minus_list}")

ans = 0

while plus_list:
    pl = plus_list.pop()

    ans += pl[0] * 2

while minus_list:
    ml = minus_list.pop()

    ans += abs(ml[0]) * 2

if max_minus < max_plus:
    ans -= max_plus
else:
    ans -= max_minus

print(ans)

