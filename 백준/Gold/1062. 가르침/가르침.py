"""
## 1062번 : 가르침

## 문제
1. K 개의 글자를 가르칠 시간밖에 없음

2. 가르치고 난 후에는, 학생들은 그 K개의 글자로만 이루어진 단어만을 읽을 수 있음

3. 어떤 K개의 글자를 가르쳐야 학생들이 읽을 수 있는 단어의 개수가 최대가 되는지 고민

4. 남극언어의 모든 단어는 "anta" 로 시작되고, "tica" 로 끝남
- 남극단어에 단어는 N개 밖에 없다고 가정
- 학생들이 읽을 수 있는 단어의 최댓값을 구하는 프로그램 작성하기

## 입력
1. 단어의 개수 N, K
- 0 < N <= 50
- 0 <= K < 26

2. 둘째줄부터 N개의 줄에 남극 언어의 단어가 주어짐
- 단어는 영어 소문사로만 이루어져 있고, 길이가 8보다 크거나 같음 ( antatica 의 길이 이상 )
- 모든 단어는 중복되지 않음

## 출력
1. K 개의 글자를 가르칠 때, 학생들이 읽을 수 있는 단어 개수의 최댓값 출력하기

## 풀이
1. 예제를 보니, antatica 에 포함되는 단어도 가르쳐야함
- a, n, t, i, c 5글자는 무조건 가르쳐야 적어도 글자를 읽을 수 있는 기초가 쌓임
- 그렇지않으면 단어를 못읽음

2. 위의 5글자를 제외한 나머지 글자들 완전탐색

"""
import sys
from itertools import combinations

input = sys.stdin.readline

단어갯수, 글자수 = map(int, input().split())

# 예외 처리, a, n, t, i, c 는 무조건 포함
if 글자수 < 5:
    print(0)
    exit(0)
elif 글자수 == 26:
    print(단어갯수)
    exit(0)
else:
    글자수 -= 5

# 차집합
words = [set(input().strip()) - {'a', 'n', 't', 'i', 'c'} for _ in range(단어갯수)]

# 배워야 할 전체 알파벳
알파벳 = set()

for word in words:
    for w in word:
        알파벳.add(w)

# 모든 알파벳을 배울 수 있다면 다 읽을 수 있음
if len(알파벳) < 글자수:
    print(단어갯수)
else:
    arr = list(combinations(알파벳, 글자수))
    _max = 0
    for arr in combinations(알파벳, 글자수):
        arr = set(arr) | {'a', 'n', 't', 'i', 'c'}
        ans = 0
        for word in words:
            for char in word:
                if char not in arr:
                    break
            else:
                ans += 1

        if ans > _max:
            _max = ans
    print(_max)