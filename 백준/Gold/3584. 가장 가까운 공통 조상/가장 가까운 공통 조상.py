"""
## 가장 가까운 공통 조상

## 문제
1. 루트가 있는 트리가 주어짐

2. 그 트리 상의 두 정점이 주어질 때 그들의 가장 가까운 공통 조상은 다음과 같이 정의됨
- 두 노드를 모두 자손으로 가지면서 깊이가 가장 깊은 노드 ( 즉 두 노드와 가장 가까운 노드 )

3. 루트가 있는 트리가 주어지고, 두 노드가 주어질 때 그 두 노드의 가장 가까운 공통 조상을 찾는 프로그램 작성하기

## 입력
1. 테스트 케이스의 개수 T

2. 각 테스트 케이스마다, 첫째 줄에 트리를 구성하는 노드의 수 N 이 주어짐 ( 2 <= N <= 10000 )

3. N-1 개의 줄에 트리를 구성하는 간선 정보가 주어짐
- A, B ( A 가 B 의 부모 )

3. 테스트 케이스의 마지막 줄에 가장 가까운 공통 조상을 구할 두 노드가 주어짐

## 출력
1. 각 테스트 케이스 별로 주어진 두 노드의 가장 가까운 공통 조상 출력하기

## 풀이
1. 트리 구성하기

2. DFS 탐색을 진행하여, 가장 가까운 부모 찾기
"""
import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

t = int(input())

def dfs(node, node_list):
    if len(tree[node]) == 0: # 루트 노드일경우
        return

    for next_node in tree[node]:
        if next_node: # 부모가 있는 경우
            node_list.append(next_node)
            dfs(next_node, node_list)

for _ in range(t):
    n = int(input())

    tree = [[] for _ in range(n+1)]
    # 간선 정보 추가하기 ( 자식, 부모 )
    for _ in range(n-1):
        parent, child = map(int, input().split())
        tree[child].append(parent)
    # 두 노드
    node1, node2 = map(int, input().split())

    node1_parent_list = [node1]
    dfs(node1, node1_parent_list)

    node2_parent_list = [node2]
    dfs(node2, node2_parent_list)

    check = False

    for n1 in node1_parent_list:
        for n2 in node2_parent_list:
            if n1 == n2:
                print(n1)
                check = True
                break
        if check:
            break

