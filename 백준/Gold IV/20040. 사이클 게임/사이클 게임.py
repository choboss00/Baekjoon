"""
## 사이클 게임

## 문제
1. 사이클 게임 : 두 명의 플레이어가 차례대로 돌아가며 진행하는 게임

2. 선 플레이어가 홀수 번째 차례를, 후 플레이어가 짝수 번째 차례를 진행함

3. 게임 시작 시 0 ~ n-1 까지 고유한 번호가 부여된 평면 상의 점 n 개가 주어짐
- 이 중 어느 세 점도 일직선 위에 놓이지 않음

4. 매 차례마다 플레이어는 두 점을 선택해서 이를 연결하는 선분을 그음 ( 연결 )
- 이전에 그린 선분을 다시 그을 수는 없지만 이미 그린 다른 선분과 교차하는 것은 가능함

5. 게임을 진행하다가 처음으로 사이클을 완성하는 순간 게임이 종료됨

6. 사이클 C 는 플레이어가 그린 선분들의 부분집합으로, 다음 조건을 만족함
- C 에 속한 임의의 선분의 한 끝점에서 출발하여 모든 선분을 한 번씩만 지나서 출발점으로 되돌아올 수 있음

7. 게임의 진행 상황이 주어지면 몇 번째 차례에서 사이클이 완성되었는지, 혹은 아직 게임이 진행중인지를 판단하는 프로그램 작성하기

## 입력
1. 첫 번째 줄에는 점의 개수를 나타내는 정수 n, 진행된 차례의 수를 나타내는 정수 m
- 3 <= n <= 500000, 3 <= m <= 1000000

2. n개의 점에는 0 부터 n-1 까지 고유 번호가 부여되어 있으며, 이 중 어느 세 점도 일직선 위에 놓이지 않음

3. 이어지는 m 개의 입력 줄에는 각각 i번째 차례에 해당 플레이어가 선택한 두 점의 번호가 주어짐
- 1 <= i <= m

## 출력
1. m 번째 차례까지 게임을 진행한 상황에서 이미 게임이 종료되었다면 사이클이 처음으로 만들어진 차례의 번호를 양의 정수로 출력

2. m 번의 차례를 모두 처리한 이후에도 종료되지 않았다면 0 출력하기

## 풀이
1. union - find

"""
import sys

def find(parents, node):
    if node == parents[node]: # 자기 자신이 루트 노드일 경우
        return node
    parents[node] = find(parents, parents[node]) # 부모 노드로 올라가기 ( 경로압축 )
    return parents[node]

def union(parents, nodeA, nodeB, idx):
    nodeA = find(parents, nodeA)
    nodeB = find(parents, nodeB)

    if nodeA == nodeB:
        print(idx + 1)
        exit(0)


    if nodeA < nodeB:
        parents[nodeB] = nodeA
    else:
        parents[nodeA] = nodeB

input = sys.stdin.readline

n, m = map(int, input().split())
# 처음엔 자기 자신이 루트 노드
parents = [i for i in range(n)]

for i in range(m):
    a, b = map(int, input().split())

    union(parents, a, b, i)

print(0)

