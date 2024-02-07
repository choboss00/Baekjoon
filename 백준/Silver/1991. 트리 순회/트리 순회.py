"""
## 트리 순회

## 문제
1. 이진 트리를 입력받아 전위 순회, 중위 순회, 후위 순회한 결과를 출력하는 프로그램 작성하기

## 입력
1. 이진 트리의 노드의 개수 N

2. 둘째줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어짐
- 노드의 이름은 A 부터 차례대로 알파벳 대문자로 매겨짐
- 항상 A 가 루트 노드가 됨
- 자식 노드가 없는 경우 . 으로 표현함

## 출력
1. 전위 순회, 중위 순회, 후위 순회한 결과 출력하기
- 각 줄에 N개의 알파벳을 공백 없이 출력하면 됨
"""

tree = {}
class Node:
    def __init__(self, item, left_node, right_node):
        self.item = item
        self.left_node = left_node
        self.right_node = right_node

def preorder(node):
    if node.item != '.':
        print(node.item, end='')
    if node.left_node != '.':
        preorder(tree[node.left_node])
    if node.right_node != '.':
        preorder(tree[node.right_node])

def inorder(node):
    if node.left_node != '.':
        inorder(tree[node.left_node])
    if node.item != '.':
        print(node.item, end='')
    if node.right_node != '.':
        inorder(tree[node.right_node])

def postorder(node):
    if node.left_node != '.':
        postorder(tree[node.left_node])
    if node.right_node != '.':
        postorder(tree[node.right_node])
    if node.item != '.':
        print(node.item, end='')


n = int(input())

for i in range(n):
    p, left, right = map(str, input().split())
    tree[p] = Node(p, left, right)

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])
