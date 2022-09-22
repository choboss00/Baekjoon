import sys

N, M = map(int, sys.stdin.readline().split())
card_list = list(map(int, sys.stdin.readline().split()))

card_max = []
for i in range(0, N):
    for j in range(i, N):
        for k in range(j, N):
            if(i == j or j == k):
                pass
            else:
                card_max.append(card_list[i] + card_list[j] + card_list[k])

card_max = list(set(card_max))

card_max_2 = []

for i in range(0, len(card_max)):
    if(card_max[i] <= M):
        card_max_2.append(card_max[i])

print(max(card_max_2))
