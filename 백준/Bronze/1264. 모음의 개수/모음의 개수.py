"""
## 모음의 개수

## 문제
1. 영문 문장을 입력받아 모음의 개수를 세는 프로그램 작성하기

## 입력
1. 여러 개의 테스트 케이스

2. 끝 : # 입력

## 출력
1. 각 줄마다 모음의 개수를 세서 출력하기
"""

while True:
    s = input()

    if s == '#':
        break

    cnt = 0

    for s_i in s:
        if s_i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            cnt += 1
    print(cnt)