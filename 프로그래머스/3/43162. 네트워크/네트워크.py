# find
def find(parents, x):
    # 만약 부모 노드가 자기자신이 아닐경우
    if parents[x] != x:
        # 루트 노드를 찾을 때 까지 재귀적으로 호출
        return find(parents, parents[x])
    return x
    
# union
def union (parents, a, b):
    nodeA = find(parents, a)
    nodeB = find(parents, b)
    
    if nodeA < nodeB:
        parents[nodeB] = nodeA
    else:
        parents[nodeA] = nodeB

def solution(n, computers):
    answer = 0
    
    # 부모 노드
    parents = [i for i in range(n)]
    
    # 연결하기
    for i in range(n):
        for j in range(n):
            # 자기자신은 제외
            if i != j:
                # 연결된 경우
                if computers[i][j] == 1:
                    # 연결하기
                    union(parents, i, j)
    
    ans = set()
    for i in range(n):
        ans.add(find(parents, parents[i]))
    
    return len(ans)


"""
1. 네트워크 : 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태
2. 컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열
3. 네트워크의 개수 return

풀이
1. union - find
"""