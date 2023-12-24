"""
## 1251번 : 단어 나누기

## 문제 : 단어 나누기
1. 단어가 주어지면 다음과 같은 과정 진행
- 세 단어로 나누기
- 각각 뒤집기
- 합치기

2. 단어가 주어지면, 이렇게 만들 수 있는 단어 중에서 사전순으로 가장 앞서는 단어를 출력하는 프로그램 작성하기

## 입력
1. 단어
- 3 <= 길이 <= 50

## 출력
1. 구하고자 하는 단어 출력

## 풀이
1. 반복문 사용해서 단어 쪼개기

2. 과정에 맞게 진행

"""
import sys

input = sys.stdin.readline

s = input().strip()
ans_list = []

for i in range(len(s)):
    # 첫번째 단어
    s1 = s[:i+1]
    s1 = s1[::-1]
    for j in range(i+1, len(s)-1):
        # 두번째 단어
        s2 = s[i+1:j+1]
        # 세번째 단어
        s3 = s[j+1:]

        # 문자열 뒤집기
        s2, s3 = s2[::-1], s3[::-1]

        # 합치기
        ans_list.append(s1+s2+s3)

ans_list.sort()

print(ans_list[0])


