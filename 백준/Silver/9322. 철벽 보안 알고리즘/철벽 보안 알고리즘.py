"""
## 철벽 보안 알고리즘

## 문제
1. 공개키만을 이용하는 암호화 체계

2. 한 단어 : 1 ~ 10개의 대문자(A-Z)들로 이루어진 문자열
- 한 문장은 공백으로 구분된 단어들로 이루어짐

3. 제 1 공개키 : 최대 한 번만 사용된 단어들로 되어있음

3. 제 2 공개키 : 제 1 공개키의 단어들을 재배치하여 만들어짐

4. 평문 ( 암호화 되지 않은 문장 ) : 제 1 공개키와 같이 여러 단어들로 되어있지만, 제 1 공개키와 다르게 각 단어들은 중복 가능

5. 암호문 ( 암호화 된 문장 ) : 평문을 제 2 공개키를 만든 규칙의 반대로 재배치하여 만들어짐

6. 주어진 2개의 공개키와 암호문으로 평문 복구하기

## 입력
1. 테스트 캐이스 수 ( < 100 )

2. 각 테스트케이스마다 아래 항목들을 한 줄씩 입력받음
- 한 문장의 단어 수
- 제 1 공개키
- 제 2 공개키
- 암호문

## 출력
1. 각 케이스마다 암호문을 해독한 평문을 한줄에 출력하기

## 풀이
1. 딕셔너리 사용

"""
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input()) # 한 문장의 단어 수
    first_list = list(input().strip().split()) # 제 1 공개키
    second_list = list(input().strip().split()) # 제 2 공개키

    # 공개키 두개를 합쳐서 딕셔너리 ( 해싱 )
    first_dict = {}
    second_dict = {}

    for i in range(n):
        if first_list[i] not in first_dict:
            first_dict[first_list[i]] = i

        if second_list[i] not in second_dict:
            second_dict[second_list[i]] = i

    # 암호문
    encod = list(input().strip().split())
    # 평문
    decod = []

    idx = 0
    # 바뀐 순서에 맞춰서 넣어주기
    for key, value in second_dict.items():
        decod.append([first_dict[key], encod[idx]])
        idx += 1

    decod.sort(key= lambda x : x[0])

    for _idx, _str in decod:
        print(_str, end=' ')
