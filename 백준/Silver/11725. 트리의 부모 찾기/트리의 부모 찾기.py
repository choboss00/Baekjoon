"""
11725번. 트리의 부모 찾기

루트 : 1
각 노드의 부모를 구하는 프로그램 작성하기

"""
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int, input().split())
    # 양방향
    tree[a].append(b)
    tree[b].append(a)

# 방문 표시
visited = [0 for _ in range(n+1)]

queue = deque()

queue.append((1))
while queue:
    node = queue.popleft()

    for next_node in tree[node]:
        if visited[next_node] == 0:
            visited[next_node] = node
            queue.append(next_node)

print(*visited[2:], sep="\n")