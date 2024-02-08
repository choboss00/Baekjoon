"""
## 완전 이진 트리

## 문제
1. 도시의 도로 : 깊이가 K 인 완전 이진 트리

2. 도시에 있는 모든 빌딩에 들어갔고, 들어간 순서대로 번호를 종이에 적어놓았음

3. 어떤 순서로 도시를 방문해냈는지 기억하고 있음
- inorder 구현

4. 종이에 적은 순서가 모두 주어졌을 때, 각 레벨에 있는 빌딩의 번호를 구하는 프로그램 작성하기

## 입력
1. K

2. 방문한 빌딩의 번호가 순서대로 주어짐

## 출력
1. K개의 줄에 걸쳐서 정답 출력하기

2. 출력 : 왼쪽에서 오른쪽 순서대로 출력하기

## 풀이
1. 분할정복
"""
import sys

input = sys.stdin.readline

def recur(nodes, depth, level):
    if depth == level:
        return
    nodes_length = len(nodes) // 2

    ans_list[level].append(nodes[nodes_length])

    recur(nodes[:nodes_length], depth, level + 1)
    recur(nodes[nodes_length+1:], depth, level + 1)



n = int(input())
n_list = list(map(int, input().split()))

ans_list = [[] for _ in range(n)]

recur(n_list, n, 0)

for ans in ans_list:
    print(*ans)