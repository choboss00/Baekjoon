"""
1543번. 문서 검색 ( 실버 4 )

브루트포스 - 다구하기

"""
import sys

input = sys.stdin.readline

n = input().strip()
m = input().strip()
# 다른 문자로 교체
l = n.replace(m,'@')
answer = 0
for i in l:
    if i == '@':
        answer += 1

print(answer)
