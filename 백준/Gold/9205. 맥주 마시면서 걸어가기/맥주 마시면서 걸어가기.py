"""
## 맥주 마시면서 걸어가기

## 문제
1. 출발 : 상근이네 집

2. 맥주 한 박스를 들고 출발함
- 맥주 한 박스에는 맥주가 20개 들어있음

3. 목이 마르면 안되기 땜누에 50미터에 한 병씩 마시려고 함
- 즉 50미터를 가려면 그 직전에 맥주 1병을 마셔야 함

4. 편의점에 들렀을 때, 빈 병은 버리고 새 맥주 병을 살 수 있음
- 박스에 들어있는 맥주는 20병을 넘을 수 없음 ( 최대 20개 )

5. 편의점을 나선 직후에도 50미터를 가기 전에 맥주 한 병을 마셔야 함

6. 편의점, 상근이네 집, 펜타포트 락 페스티벌의 좌표가 주어질 때, 페스티벌에 도착할 수 있는지 구하는 프로그램 작성하기

## 입력
1. 테스트 케이스의 개수 t

2. 각 테스트 케이스의 첫째 줄에는 맥주를 파는 편의점의 개수 n 이 주어짐
- 0 <= n <= 100

3. 다음 n+2 개 줄에는 상근이네 집, 편의점, 펜타포트 락 페스티벌 좌표가 주어짐
- 각 좌표는 두 정수 x 와 y 로 이루어져 있음

4. 송도는 직사각형 모양으로 생긴 도시임
- 두 좌표 사이의 거리는 x 좌표의 차이 + y 좌표의 차이

## 출력
1. 각 테스트 케이스에 대해서 페스티벌에 갈 수 있는 경우 happy, 그렇지 않으면 sad 출력하기

## 풀이
1. 거리 계산 : 맨해튼 거리

2. 처음은 맥주가 20개 들어있으니, 최대 1000미터까지 이동할 수 있음 ( x : 500, y : 500 이런식 )

3. 편의점을 들러서 가는 경우와 안들러도 되는 경우가 있을 듯 하다.
- 처음 좌표 저장
- 편의점, 도착 지점 구분하기

4. 맨해튼 거리로 구했을 때, 갈 수 없는 경우 sad 출력하기

"""
import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    x, y = map(int, input().split())

    n_list = [list(map(int, input().split())) for _ in range(n)]

    end_x, end_y = map(int, input().split())

    queue = deque()

    queue.append([x, y])
    # 방문 처리
    visited = [False for _ in range(n)]

    # 갈수있는지 체크
    check = False

    while queue:
        now_x, now_y = queue.popleft()

        if abs(now_x - end_x) + abs(now_y - end_y) <= 1000:
            print("happy")
            check = True
            break

        for i in range(n):
            if not visited[i]:
                new_x, new_y = n_list[i][0], n_list[i][1]

                if abs(new_x - now_x) + abs(new_y - now_y) <= 1000:
                    queue.append([new_x, new_y])
                    visited[i] = True

    if not check:
        print("sad")


