"""
## 컨테이너 벨트 위의 로봇

## 문제
1. 길이가 N 인 컨베이어 벨트가 있고, 길이가 2N 인 벨트가 이 컨베이어 벨트를 위아래로 감싸며 돌고 있음
- 벨트는 2N 개의 칸으로 나뉘어져 있음

2. 벨트가 한 칸 회전하면 1번부터 2N-1 번까지의 칸은 다음 번호의 칸이 있는 위치로 이동, 2N번 칸은 1번 칸의 위치로 이동
- i번 칸의 내구도는 Ai
- 1번 칸이 있는 위치 : 올리는 위치
- N번 칸이 이쓴 위치 : 내리는 위치

3. 컨테이어 벨트에 박스 모양 로봇을 하나씩 올리려고 함
- 로봇은 올리는 위치 ( 1번 칸 ) 에만 올릴 수 있음
- 언제든지 로봇이 내리는 위치에 도달하면 그 즉시 내림
- 로봇은 컨베이어 벨트 위에서 스스로 이동할 수 있음
- 로봇을 올리는 위치에 올리거나, 어떤 칸으로 이동하면 그 칸의 내구도는 즉시 1만큼 감소함

4. 로봇을 옮기는 과정
- 벨트가 각 칸에 있는 로봇과 함께 한칸 회전함 ( deque 를 쓰면 좋을 듯 )
- 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동함 ( 이동할 수 없다면 가만히 있음 )
- 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아있어야 함
- 올리는 위치에 있는 칸의 내구도가 0 이 아니라면 ( 1번 칸의 내구도 체크 ) 올리는 위치에 로봇을 올림
- 내구도가 0인 칸의 개수가 K개 이상이라면 과정 종료, 그렇지 않다면 위 과정을 반복함

5. 종료되었을 때 몇 번째 단계가 진행 중이었는지 구해보기
- 가장 처음 수행되는 단계는 1번째 단계 ( 1부터 시작 )

## 입력
1. 첫째 줄에 N, K ( 벨트, 내구도 종료 카운트 )

2. A1.. A2N ( 각 칸의 내구도 )

## 출력
1. 몇 번째 단계가 진행 중일 때 종료되었는지 출력하기

## 풀이
1. deque 사용 ( 벨트가 회전하기 때문 )

2. 내구도에 신경쓰며 단계 카운트하기
"""
import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
belts = deque(map(int, input().split()))
robots = deque([0 for _ in range(n)])

durability = belts.count(0) # 내구도가 0 인 벨트의 개수 카운트

ans = 0

while durability < k:
    # 벨트가 각 칸에 있는 로봇들과 함께 한 칸 회전함
    belts.rotate(1)
    robots.rotate(1)

    # 로봇 내리기
    if robots[-1] == 1:
        robots[-1] = 0

    idx = n - 2

    # 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동함. 이동할 수 없다면 가만히 있음
    while idx > 0:
        # 이동할 수 있는 경우 ( 이전 로봇이 있어야 하고, 내구도가 있어야 하고, 로봇이 없어야 함 )
        if robots[idx] == 1 and belts[idx+1] > 0 and robots[idx+1] == 0:
            belts[idx+1] -= 1
            # 내구도 개수 카운트
            if belts[idx+1] == 0:
                durability += 1

            # 로봇 옮기기
            robots[idx], robots[idx+1] = 0, 1

        idx -= 1 # 다음 로봇으로 이동

    # 로봇 내리기
    if robots[-1] == 1:
        robots[-1] = 0

    # 올리는 위치에 있는 칸의 내구도가 0 이 아니라면 올리는 위치에 로봇을 올림
    if belts[0] > 0:
        robots[0] = 1 # 로봇 올리기

        belts[0] -= 1 # 로봇 올리면 내구도가 감소함

        if belts[0] == 0:
            durability += 1

    # 단계 카운트
    ans += 1

print(ans)