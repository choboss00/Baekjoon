"""
25192번. 인사성 밝은 곰곰이 ( 실버 4 )

새로운 사람 입장 -> 인사
채팅방 기록 수집해서 인사 횟수 구하기

enter -> 새로운 사람이 채팅방에 입장
새로운 사람이 입장한 이후 ( enter 이후 )
처음 채팅을 입력하는 사람은 반드시 인사를 함
-> 인사 횟수 구하기

"""
import sys

input = sys.stdin.readline

n = int(input())
# 사전
d = dict()
answer = 0
for i in range(n):
    # 문자열 받기
    s = input().strip()

    if s == 'ENTER':
        answer += len(d)
        # 사전 초기화
        d = dict()
    else:
        if s not in d:
            d[s] = 1

    if i == n-1:
        if s != 'ENTER':
            answer += len(d)
print(answer)