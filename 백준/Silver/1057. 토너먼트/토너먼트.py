"""
1057번. 토너먼트 ( 실버 4 )

참가자 1 ~ n명
인접 번호끼리 스타 진행
-> 이긴사람은 다음 라운드 진출
-> 진 사람은 탈락

만약 그 라운드의 참가자가 홀수
-> 마지막 번호 자동 진출

임한수 vs 김지민

1라운드에서 김지민의 번호와 임한수의 번호가 주어질 때
몇라운드에서 대결하는지?

n : 참가자의 수
m : 김지민의 번호
k : 임한수의 번후

"""
import sys

input = sys.stdin.readline

n,m,k = map(int, input().split())

m,k = min(m,k), max(m,k)

# 정답
cnt = 1
# 만나는 경우 : m이 홀수, k가 짝수 and 값이 1차이 ( 1 , 2 )
while True:
    # 예외처리 ( 서로 대결하지 않을 경우 )
    if m == 1 and k == 1:
        print(-1)
        exit(0)
    if m % 2 == 1 and k % 2 == 0 and abs(m-k) == 1:
        print(cnt)
        exit(0)
    else:
        if m % 2 == 1:
            m = m // 2 + 1
        else:
            m = m // 2

        if k % 2 == 1:
            k = k // 2 + 1
        else:
            k = k // 2
        cnt += 1



