"""
## 나무 탈출

## 문제
1. N개의 정점이 있는 트리 모양으로 생긴 게임판, 몇 개의 게임말로 이루어짐
- 트리의 각 정점엔느 1번 ~ N번까지 번호가 붙어있음
- 1번 : 루트 노드라 불리며, 이 루트 노드를 중심으로 부모 - 자식 관계가 만들어짐
- 자식이 없는 노드 : 리프 노드

2. 게임
- 두 사람이 번갈아 가면서 게임판에 놓여있는 게임말을 움직임
- 초기 : 트리의 모든 리프 노드에 게임말이 하나씩 놓여있는 채로 시작함
- 어떤 사람의 차례가 오면, 그 사람은 현재 존재하는 게임말 중 아무거나 하나를 골라 그 말이 놓여있던 노드의 부모 노드로 옮김
- 만약 그 게임말이 루트 노드에 도착했다면 그 게임말을 즉시 제거함
- 모든 과정을 마치면 다음 사람에게 차례를 넘김
- 게임말이 게임판에 존재하지 않아 고를 수 없는 사람이 지게 됨

3. 선 : 성원, 후 : 형석
- 게임 시작 전, 게임판의 모양만 보고 이 게임을 이길 수 있을지 판단하는 프로그램 만들기

## 입력
1. 트리의 정점 개수 N

2. 트리의 간선 정보

## 출력
1. 성원이가 이길 수 있으면 Yes, 아니면 No 출력

## 풀이
1. 트리의 정보가 주어져 있음

2. 리프 노드에서 노드를 하나씩 부모 노드로 옮기면서, 루트 노드의 위치까지 옮겨야함
- 서로 번갈아가면서 진행

3. 그러므로, 루트 노드에서 각 해당 리프 노드까지의 깊이를 구한 뒤, 깊이의 합 구하기

"""
import sys

sys.setrecursionlimit(200000)
def dfs(node, graph, visited):
    # 현재 위치 방문처리
    visited[node] = True

    for next_node in graph[node]:
        if not visited[next_node]: # 아직 방문하지 않은 노드 일 경우
            dist[next_node] = dist[node] + 1 # 깊이 증가
            dfs(next_node, graph, visited) # 그 다음 노드 dfs 탐색 진행

input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]
# 방문 정보
visited = [False for _ in range(N+1)]
# 각 노드의 깊이
dist = [0 for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    # 간선 연결
    graph[a].append(b)
    graph[b].append(a)

dfs(1, graph, visited)

ans = 0

for i in range(2, N+1):
    if len(graph[i]) == 1: # 리프 노드일 경우
        ans += dist[i]

if ans % 2 == 0:
    print('No')
else:
    print('Yes')