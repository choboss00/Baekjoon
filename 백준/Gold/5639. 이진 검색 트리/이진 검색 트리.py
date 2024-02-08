"""
## 이진 검색 트리

## 문제
1. 이진 검색 트리는 다음과 같은 3가지 조건을 만족하는 이진 트리
- 노드의 왼쪽 서브트리에 있는 모든 노드의 키는 노드의 키보다 작다
- 노드의 오른쪽 서브트리에 있는 모든 노드의 키는 노드의 키보다 크다
- 왼쪽, 오른쪽 서브트리도 이진 검색 트리이다

2. 이진 검색 트리를 전위 순회한 결과가 주어졌을 때, 이 트리를 후위 순회한 결과를 구하는 프로그램 작성하기
- 전위 순회 : 루트 - 왼쪽 - 오른쪽
- 후위 순회 : 왼쪽 - 오른쪽 - 루트

## 입력
1. 트리를 전위 순회한 결과가 주어짐

2. 같은 키를 가지는 노드는 없음

## 출력
1. 입력으로 주어진 이진 검색 트리를 후위 순회한 결과를 한 줄에 하나씩 출력하기

## 풀이
1. 이진 검색 트리 만들기

2. 후위 순회 진행하기
"""
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
class Node:
    def __init__(self, root, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None # 초기에는 아무것도 없는 상태

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            cur = self.root
            while True:
                if key < cur.root: # 왼쪽 노드로 이동
                    if not cur.left:
                        cur.left = Node(key)
                        break
                    else:
                        cur = cur.left # 한 칸 더 이동
                else:
                    if not cur.right:
                        cur.right = Node(key)
                        break
                    else:
                        cur = cur.right

    def postorder(self, node):
        if node.left:
            self.postorder(node.left)
        if node.right:
            self.postorder(node.right)
        print(node.root)



bst = BST()

while True:
    try:
        n = int(input())
        bst.insert(n)
    except:
        break

bst.postorder(bst.root)