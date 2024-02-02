"""
## 시험 감독

## 문제
1. N 개의 시험장, 각각의 시험장마다 응시자들이 있음

2. 감독관 : 총감독관, 부감독관
- 총감독관 : 한 시험장에서 감시할 수 있는 응시자의 수가 B 명
- 부감독관 : 한 시험장에서 감시할 수 있는 응시자의 수가 C 명

3. 각각의 시험장에 총감독관은 오직 1명만 있어야 하고, 부감독관은 여러 명 있어도 됨

4. 각 시험장마다 응시생들을 모두 감시해야 할 때, 필요한 감독관 수의 최솟값을 구하는 프로그램 작성하기

## 입력
1. 시험장의 개수 N

2. 응시자의 수 Ai

3. 감시할 수 있는 인원 수 B, C

## 출력
1. 각 시험장마다 응시생을 모두 감독하기 위해 필요한 감독관의 최소 수 출력하기

"""
import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

b, c = map(int, input().split())

ans = 0

for a in arr:
    if a < b: # 총감독관만으로 커버 가능
        ans += 1
        continue
    ans += 1 # 총 감독관 더하기
    a -= b

    a_div, a_mod = divmod(a, c)

    if a_mod == 0:
        ans += a_div
    else:
        ans += (a_div + 1)

print(ans)