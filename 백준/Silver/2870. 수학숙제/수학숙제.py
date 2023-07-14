"""
2870번. 수학숙제 ( 실버 4 )

글자 -> 숫자를 모두 찾은 뒤, 비내림차순으로 정리
숫자의 앞에 0이 있는 경우 -> 정리하면서 생략가능

"""
import sys
import re

input = sys.stdin.readline

n = int(input())

# 리스트 입력
n_list = []

for _ in range(n):
    s = input().strip()
    sub_list = list(map(int, re.findall('\d+', s)))
    for i in sub_list:
        n_list.append(i)

n_list.sort()

for ans in n_list:
    print(ans)
