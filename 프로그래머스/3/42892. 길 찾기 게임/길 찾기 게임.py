class Node:
    def __init__(self, info, num, left=None, right=None):
        self.info = info
        self.left = left
        self.right = right
        self.num = num

    def has_left(self):
        return self.left is not None
    
    def has_right(self):
        return self.right is not None

def make_BT(nodeinfo):
    nodes = [i for i in range(1, len(nodeinfo)+1)]
    
    nodes.sort(key=lambda x: (-nodeinfo[x-1][1], nodeinfo[x-1][0]))
    
    root = None
    
    for i in range(len(nodeinfo)):
        if root is None:
            root = Node(nodeinfo[nodes[0]-1], nodes[0])
        else:
            parent = root
            node = Node(nodeinfo[nodes[i]-1], nodes[i])
            
            while True:
                if node.info[0] < parent.info[0]: # x 좌표 비교
                    if parent.has_left(): # 왼쪽 자식이 존재하면
                        parent = parent.left
                        continue
                    parent.left = node
                    break
                else:
                    if parent.has_right():
                        parent = parent.right
                        continue
                    parent.right = node
                    break
    return root

def pre_order(root, answer):
    stack = [root]
    while stack:
        node = stack.pop()
        
        if node is None:
            continue
        answer[0].append(node.num)
        # stack 이기 때문에 오른쪽을 먼저 넣음 ( FILO )
        stack.append(node.right)
        stack.append(node.left)

def post_order(root, answer):
    stack = [(root, False)]
    while stack:
        node, visited = stack.pop()
        
        if node is None:
            continue
        if visited: # 현 위치가 방문한 위치일 경우
            answer[1].append(node.num)
        else:
            stack.append((node, True))
            stack.append((node.right, False))
            stack.append((node.left, False))
    

def solution(nodeinfo):
    answer = [[], []]
    
    root = make_BT(nodeinfo)
    
    pre_order(root, answer)
    post_order(root, answer)
    
    return answer

"""
## 길 찾기 게임

## 문제
1. 카카오 프렌즈를 2팀으로 나누기

2. 각 팀이 같은 곳을 다른 순서로 방문하도록 해서 먼저 순회를 마친 팀이 승리

3. 방문할 곳의 2차원 좌표 값을 구하고 각 장소를 이진트리의 노드가 되도록 구성
- 순회 방법을 힌트로 주어 각 팀이 스스로 경로를 찾도록 할 계획

4. 트리 노드 구성 규칙
- 트리를 구성하는 모든 노드의 x, y 좌표값은 정수
- 모든 노드는 서로 다른 x 값을 가짐 ( 중복되는 위치는 없음 )
- 같은 레벨에 있는 노드는 같은 y 좌표를 가짐 ( 같은 level )
- 자식 노드의 y 값은 항상 부모 노드보다 작음 ( 부모 노드가 항상 위에 위치 )
- 임의의 노드 V 의 왼쪽 서브 트리에 있는 모든 노드의 x 값은 V 의 x 값 보다 작음 ( 서브트리는 왼쪽으로 뻗어감 )
- 임의의 노드 V 의 오른쪽 서브 트리에 있는 모든 노드의 x 값은 V 의 x 값 보다 큼 ( 서브트리는 오른쪽으로 뻗어감 )

5. 이진트리를 구성하는 노드들의 좌표가 담긴 배열 nodeinfo
- nodeinfo 의 길이는 1 이상 10000 이하
- nodeinfo[i] 는 i+1 번 노드의 좌표, [x, y]
- 모든 노드의 좌표 값은 0 이상 10만 이하
- 트리의 깊이가 1000 이하 ( 재귀 함수 호출 에러 걱정 )
- 잘못된 노드 위치가 주어지는 경우는 없음

6. 노드들로 구성된 이진트리를 전위 순회, 후위 순회한 결과를 2차원 배열에 담아 return 하기

## 풀이
1. 노드들을 y 축 기준으로 정렬하기

2. 가장 먼저 오는 노드가 루트 노드

3. 현 부모 노드와 x 값 비교후, 왼쪽에 담을지 오른쪽에 담을지 결정하기

4. 순회해야하므로, list 가 아닌 class 로 변수 값 담기

"""