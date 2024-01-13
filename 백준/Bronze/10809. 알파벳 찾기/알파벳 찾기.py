"""
## 알파벳 찾기

## 문제
1. 단어 : S ( 알파벳 소문자로만 이루어진 단어 )

2. 각각의 알파벳에 대해서, 단어가 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램

## 입력
1. 단어 S

## 출력
1. a ~ z 까지 단어가 처음 등장하는 위치를 공백으로 구분해서 출력하기

## 풀이
1. 단어 s 를 문자로 쪼개기

2. 반복문을 활용하여 탐색 진행

"""

arr = [chr(i) for i in range(97, 123)]

s = input()

for i in range(len(s)):
    for j in range(len(arr)):
        if s[i] == arr[j]:
            arr[j] = i

for a in range(len(arr)):
    if type(arr[a]) == int:
        continue
    else:
        arr[a] = -1

print(*arr)