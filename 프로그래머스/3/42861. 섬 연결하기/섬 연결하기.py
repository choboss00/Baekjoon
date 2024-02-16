def find(parent, node):
    if parent[node] == node: # 루트 노드
        return node
    parent[node] = find(parent, parent[node]) # 경로 압축
    return parent[node]

def union(parent, nodeA, nodeB):
    nodeA = find(parent, nodeA)
    nodeB = find(parent, nodeB)
    
    if nodeA < nodeB:
        parent[nodeB] = nodeA
    else:
        parent[nodeA] = nodeB
        
def solution(n, costs):
    answer = 0
    # 비용순으로 정렬
    costs.sort(key=lambda x: x[2])
    
    # 루트 노드 설정
    parent = [i for i in range(n)]
    # 총 비용, 간선의 수
    edges = 0
    
    for cost in costs:
        if edges == n-1: # 다 연결된 경우
            break
        
        x = find(parent, cost[0])
        y = find(parent, cost[1])
        
        if x != y: # 서로의 루트 노드가 다를 경우
            union(parent, x, y)
            answer += cost[2]
            edges += 1
    
    return answer

"""
## 섬 연결하기

## 문제
1. n 개의 섬 사이에 다리를 건설하는 비용 costs

2. 최소의 비용으로 모든 섬이 서로 통행 가능하도록 만들 때 필요한 최소 비용 return 하는 solution 함수 작성하기

3. 다리를 여러 번 건너더라도, 도달할 수만 있으면 통행 가능하다고 봄 ( 다익스트라 )

## 제한사항
1. 1 <= n <= 100

2. coss 의 길이 : ((n-1) * n) / 2 이하

3. costs[i][0] 와 costs[i][1] 에는 다리가 연결되는 두 섬의 번호가 들어있음
- costs[i][2] 에는 이 두섬을 연결하는 다리를 건설할 때 드는 비용 ( 비용순으로 정렬 )

4. 같은 연결은 두 번 주어지지 않음
- 순서가 바뀌더라도 같은 연결로 봄

5. 모든 섬 사이의 다리 건설 비용이 주어지지 않음
- 두 섬 사이의 건설 불가능
- 연결할 수 없는 섬은 주어지지 않음

## 풀이
1. 최소 스패닝 트리
"""