from collections import deque

def solution(info, edges):
    # 트리 만들기
    tree = [[] for _ in range(len(info))]
    
    for edge in edges:
        tree[edge[0]].append(edge[1])
    
    max_sheep = 0
    # 현 위치, 양의 수, 늑대의 수, 방문한 노드 집합
    queue = deque()
    queue.append([0, 1, 0, set()])
    
    while queue:
        cur, sheep_cnt, wolf_cnt, visited = queue.popleft()
        
        max_sheep = max(max_sheep, sheep_cnt)
        # 현재 노드의 이웃 노드 추가
        visited.update(tree[cur])
                
        for next_node in visited:
            if info[next_node]:
                if sheep_cnt != (wolf_cnt + 1):
                    queue.append((next_node, sheep_cnt, wolf_cnt+1, visited - {next_node}))
            else:
                queue.append((next_node, sheep_cnt+1, wolf_cnt, visited - {next_node}))
    
    return max_sheep

"""
## 양과 늑대

## 문제
1. 이진 트리 모양의 각 노드에 늑대와 양이 한마리씩 놓여있음

2. 이 초원의 루트 노드에서 출발하여 각 노드를 돌아다니며 양을 모으려고 함

3. 각 노드를 방문할 때 마다 해당 노드에 있던 양과 늑대가 따라옴
- 개수를 누적해서 카운트해준다는 뜻

4. 모은 양의 수보다 늑대의 수가 같거나 더 많아지면 바로 모든 양을 잡아먹어버림

5. 중간에 양이 늑대에게 잡아먹히지 않도록 하면서 최대한 많은 수의 양을 모아서 다시 루트 노드로 돌아오려고 함

6. 양 또는 늑대에 대한 정보가 담긴 배열 info
- 0 : 양, 1 : 늑대
- info[0] : 항상 0 ( 루트 노드는 항상 양이 있음 )

7. 이진 트리의 각 노드들의 연결 관계를 담은 2차원 배열 edges
- [부모 노드 번호, 자식 노드 번호]
- 동일한 간선에 대한 정보가 중복해서 주어지지 않음
- 0번 노드는 항상 루트 노드임

8. 각 노드를 방문하면서 모을 수 있는 양의 최대 마릿수 리턴하는 함수 작성하기

## 풀이
1. 간선 연결한 트리 만들기

2. 양은 챙기고, 늑대는 최소한으로 가져가야 함


"""