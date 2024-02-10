"""
## 트리

## 문제
1. 리프 노드 : 자식의 개수가 0 인 노드를 말함

2. 트리가 주어졌을 때, 노드를 하나 지우고 남은 트리에서 리프 노드의 개수를 구하는 프로그램 작성하기
- 노드를 지우면 그 노드와 노드의 모든 자손이 트리에서 제거됨

## 입력
1. 트리의 노드 개수 N
- N 은 50보다 작거나 같은 자연수

2. 0 ~ N-1 번 노드까지, 각 노드의 부모가 주어짐
- 만약 부모가 없다면 -1

3. 셋째 줄에는 지울 노드의 번호가 주어짐

## 출력
1. 입력으로 주어진 트리에서 입력으로 주어진 노드를 지웠을 때, 리프 노드의 개수 출력하기

## 풀이
1. dfs 탐색
"""
import sys

input = sys.stdin.readline

n = int(input())
tree = list(map(int, input().split()))
delete_node = int(input())

def dfs(cur):
    tree[cur] = -2

    for i in range(n):
        if cur == tree[i]: # 현재 노드와 값이 같은 경우, 자식 노드임
            dfs(i)

dfs(delete_node)

ans = 0

for i in range(n):
    if tree[i] != -2 and i not in tree:
        ans += 1

print(ans)