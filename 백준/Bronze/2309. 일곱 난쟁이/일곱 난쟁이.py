"""
2309번 : 일곱 난쟁이

1. 난쟁이가 9명

2. 일곱 난쟁이의 키의 합 : 100

3. 아홉 난쟁이의 키가 주어졌을 때, 일곱 난쟁이 찾기

입력
1. 키 < 100

2. 아홉 난쟁이의 키는 모두 다름

3. 가능한 정답이 여러가지 -> 아무거나 출력

출력
1. 일곱 난쟁이의 키를 오름차순으로 출력하기
- 찾을 수 없는 경우는 없음

풀이
1. 백트래킹
"""
import sys
def back(lst, ans, level):
    if sum(ans_list) == ans and len(ans_list) == 7:
        for i in sorted(ans_list):
            print(i)
        exit(0)

    for i in range(level, 9):
        ans_list.append(lst[i])
        back(lst, ans, i+1)
        ans_list.pop()


input = sys.stdin.readline
# 난쟁이 리스트
n_list = [int(input()) for _ in range(9)]

ans_list = []
# back(list, ans, level)
back(n_list, 100, 0)
