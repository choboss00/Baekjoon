"""
1. 헛간의 개수 : N ( 2 ~ 20000 )

2. 1부터 숫자를 셈

3. 모든 헛간 : M개의 양방향 길로 이어져 있음
- A_i, B_i 로 나타냄

4. 냄새는 1번 헛간에서의 거리가 멀어질수록 감소함

"""
from collections import defaultdict, deque

N, M = map(int, input().split())

n_dict = defaultdict()

for i in range(1, N+1):
    n_dict[i] = []

#print(f"딕셔너리 초기화 : {n_dict}")

for _ in range(M):
    a, b = map(int, input().split())
    n_dict[a].append(b)
    n_dict[b].append(a)

#print(f"딕셔너리 업데이트 : {n_dict}")
# 방문처리
visited = [False] * (N+1)
# 값을 저장할 리스트
ans_list = [[0,i] for i in range(N+1)]

queue = deque()

queue.append((1,0))
visited[1] = True

while queue:
    key, cnt = queue.popleft()

    for i in n_dict[key]:
        if not visited[i]:
            queue.append((i, cnt+1))
            visited[i] = True
            ans_list[i][0] = cnt+1


ans_list.sort(key=lambda x:(-x[0], x[1]))

#print(ans_list)

cnt = 0
_max = ans_list[0][0]

for c, idx in ans_list:
    if _max == c:
        cnt += 1
    else:
        break

print(ans_list[0][1], ans_list[0][0], cnt)
