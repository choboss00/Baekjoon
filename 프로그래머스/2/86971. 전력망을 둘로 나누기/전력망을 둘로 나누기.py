def solution(n, wires):
    graph = [[] for _ in range(n+1)]
    
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    
    def dfs(node, parent):
        cnt = 1
        for child in graph[node]:
            if child != parent:
                cnt += dfs(child, node)
        return cnt
    
    min_diff = float("inf")
    
    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        
        cnt_a = dfs(a, b)
        cnt_b = n - cnt_a
        
        min_diff = min(min_diff, abs(cnt_a - cnt_b))
        
        graph[a].append(b)
        graph[b].append(a)
    
    return min_diff

"""
## 문제

## 전력망을 둘로 나누기

1. N개의 송전탑이 전선을 통해 하나의 트리 형태로 연결되어 있음

2. 이 전선들 중 하나를 끊어서 현재의 전력망 네트워크를 2개로 분할하려고 함

3. 이때, 두 전력망이 갖게 되는 송전탑 개수를 최대한 비슷하게 맞추고자 함

4. 송전탑의 개수 N, 전선의 정보 WIRES
- N : 2 이상, 100 이하인 자연수
- WIRES : 길이가 N-1 인 정수형 2차원 배열
- [V1, V2] : 전력망의 V1번 송전탑과 V2번 송전탑이 전선으로 연결되어 있음

5. 전선들 중 하나를 끊어서 송전탑 개수가 가능한 비슷하도록 두 전력망으로 나누었을 때

6. 두 전력망이 가지고 있는 송전탑의 개수 차이 ( 절대값 ) 를 return 하는 solution 함수 작성

## 풀이
1. 하나의 간선을 끊어야 함

2. N-2 개의 간선들의 정보를 가지고, 완전 탐색하여 각 노드들의 갯수를 카운트하기

3. 2번 과정을 완전 탐색
"""