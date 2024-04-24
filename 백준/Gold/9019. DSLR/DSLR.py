from collections import deque
import sys

T = int(input())
input = sys.stdin.readline

def bfs(a, b):
    global new_num
    queue = deque()

    queue.append([a, ''])

    while queue:
        num, str_list = queue.popleft()
        #print("현재 queue 에 들어있는 값 : ", queue)

        # 문자형태를 숫자로 변환 후 계산하기
        #print("명령어를 취하기 전 : ", int_num)

        if num == b:
            return str_list

        for s in ['D', 'S', 'L', 'R']:
            if s == 'D':
                dn = (num * 2) % 10000
                #print(f"현재 명령어 : {s}, 현재 값 : {dn}")
                if not visited[dn]:
                    visited[dn] = True
                    queue.append([dn, str_list + s])
            elif s == 'S':
                sn = num - 1

                if sn == -1:
                    sn = 9999

                #print(f"현재 명령어 : {s}, 현재 값 : {sn}")

                if not visited[sn]:
                    visited[sn] = True
                    queue.append([sn, str_list + s])

            elif s == 'L':
                ln = (num % 1000) * 10 + num // 1000

                if not visited[ln]:
                    visited[ln] = True
                    queue.append([ln, str_list + s])

            elif s == 'R':
                rn = (num % 10) * 1000 + num // 10

                if not visited[rn]:
                    visited[rn] = True
                    queue.append([rn, str_list + s])

for _ in range(T):
    A, B = map(int, input().split())

    visited = [False for _ in range(10001)]
    # 방문처리
    visited[A] = True

    # A 값을 B 로 만들기 위한 탐색 진행
    print(bfs(A, B))