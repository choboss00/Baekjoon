"""
10971번. 외판원 순회 2 ( 실버 2 )

1 ~ n 번까지 번호가 매겨져 있는 도시
도시 사이 길 존재 ( 없을 수도 있음 )

어느 한 도시에서 출발, n개의 도시를 모두 거쳐
다시 원래의 도시로 돌아오는 순회 여행 경로 계획
-> 가장 적은 비용을 들이는 계획 세우기

1 -> 3 -> 4 -> 2 -> 1 : 35

백트래킹으로
1 -> 2 -> 3 -> 4 -> 1 부터 차례대로 계산하기

"""
import sys

input = sys.stdin.readline

n = int(input())
# 테이블 생성
table = []
for i in range(n):
    table.append(list(map(int, input().split())))

visited = [False] * n
# cost 비용을 담는 리스트
c_list = []
# 순회를 할지 안할지 모르는 임시 리스트
temp_list = []

def dfs(depth):
    if depth == n:
        # 첫번째 원소 넣기
        temp_list.append(temp_list[0])
        # 금액
        c = 0
        for i in range(n):
            if table[temp_list[i]][temp_list[i+1]] == 0:
                temp_list.pop()
                return
            c += table[temp_list[i]][temp_list[i+1]]
        c_list.append(c)
        temp_list.pop()
        return

    for i in range(n):
        # 아직 방문하지 않은 노드일 경우
        if not visited[i]:
            temp_list.append(i)
            visited[i] = True
            dfs(depth + 1)
            visited[i] = False
            temp_list.pop()

dfs(0)

print(min(c_list))

