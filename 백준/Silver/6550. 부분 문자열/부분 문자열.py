"""
## 부분 문자열

## 문제
1. 2개의 문자열 s와 t가 주어짐

2. s 가 t 의 부분 문자열인지 판단하는 프로그램 작성하기
- 방법 : t에서 몇 개의 문자를 제거하고 이를 순서를 바꾸지 않고 합쳤을 경우 s가 되는 경우
- 즉 t 에서 문자 몇개 제거 -> s 가 되는지?

## 입력
1. 여러 개의 테스트 케이스
- try - except

2. 문자열 s 와 t 가 빈칸을 사이에 두고 들어옴
- s 와 t의 길이는 10만을 넘지 않음

## 출력
1. s 가 t 의 부분 문자열인 경우 Yes, 그렇지않으면 No 출력하기

## 풀이
1. s 와 t 의 문자열을 비교해야 함

2. s 와 t 의 앞부분부터 차례대로 비교하면서, 다른 부분이 있을 경우 빼버리기

3. 만약 t 의 길이가 s 보다 작아질 경우, 종료

"""
import sys
from collections import deque

input = sys.stdin.readline

while True:
    try:
        s, t = input().split()
        t = deque(t)
        # 초기 예외처리
        if len(s) > len(t):
            print('No')
            break

        idx = 0
        check = False

        while t:
            if idx == len(s):
                print('Yes')
                check = True
                break
            # 원소 비교하기
            st = t.popleft()

            if s[idx] == st:
                idx += 1

        if idx == len(s) and not check:
            print('Yes')
        elif idx < len(s) and not check:
            print('No')
    except:
        break


