"""
1246번. 온라인 판매 ( 실버 4 )

n 개의 달걀, m 명의 고객
각각의 i번째 고객은 각자 달걀 하나를 Pi 가격 이하로 구매 가능
한명당 1개씩 판매, 수익은 최대로

A 가격에 달걀을 팜
-> Pi 는 A 가격보다 크거나 같은 모든 고객은 달걀을 구매

정렬 후, 하나씩 계산

"""
import sys

input = sys.stdin.readline

n,m = map(int, input().split())
n_list = []

for i in range(m):
    n_list.append(int(input()))

n_list.sort(reverse=True)

ans = [0,0]

# 한명에게 계란을 주고, 계란이 다 떨어지거나 사람에게 다 줬을 때 종료
for i in range(m):
    # 계란 수 보다 인원 수가 더 많을 때 종료
    if i+1 > n:
        break

    if ans[0] < n_list[i] * (i+1):
        ans[0], ans[1] = n_list[i] * (i+1), n_list[i]

print(ans[1], ans[0])



