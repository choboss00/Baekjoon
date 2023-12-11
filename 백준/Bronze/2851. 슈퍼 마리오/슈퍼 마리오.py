"""
## 2851번 : 슈퍼 마리오

## 문제
1. 10개의 버섯이 일렬로 놓여져 있음
- 이 버섯을 먹으면 점수를 받음

2. 버섯을 처음부터 나온 순서대로 집으려고 함
- 모든 버섯을 집을 필요는 없고, 중간에 중단 가능
- 중단시, 그 이후에 나온 버섯은 모두 먹을 수 없음
- 첫 버섯을 먹지 않았다면, 그 이후 버섯도 모두 먹을 수 없음

3. 받은 점수의 합을 최대한 100에 가깝게 만들기

## 입력
1. 10개의 버섯

## 출력
1. 점수 출력
- 100 에 가까운 수가 2개일 경우, 큰 값 선택

## 풀이
1. 100 에 가까워질 때 까지 더하기

2. 100 에 가장 가까워졌을 때, 그 다음 값을 더하고 비교하기
"""
import sys

input = sys.stdin.readline

ans = 0
l = []

for _ in range(10):
    l.append(int(input()))

for i in range(10):
    ans += l[i]

    if ans == 100:
        print(ans)
        exit(0)

    if ans > 100:
        a = abs(ans - 100)
        b = abs(ans - l[i] - 100)

        if a <= b:
            print(ans)
        else:
            print(ans - l[i])

        exit(0)

print(ans)