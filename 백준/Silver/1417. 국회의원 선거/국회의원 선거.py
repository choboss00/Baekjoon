"""
1417번 : 국회의원
## 문제
1. 각 사람들이 누구를 찍을 지 미리 읽을 수 있음
- 어떤 사람이 누구를 찍을 지 정했으면, 반드시 그 선거때 그 사람을 찍음

2. 국회의원 후보 : n명

3. 그 마을의 주민 m명의 마음을 모두 읽었음

4. 다솜이 : 기호 1번
- 사람들의 마음을 읽어서 자신을 찍지 않으려는 사람을 돈으로 매수해서 국회의원에 당선이 돠려고 함

5. 다른 모든 사람의 득표수 보다 많은 득표수를 가질 때, 그 사람이 국회의원에 당선됨

6. 다솜이가 매수해야하는 사람의 최솟값 출력하기

## 입력
1. 후보의 수 n

2. 후보를 찍으려고 하는 사람의 수

## 출력
1. 다솜이가 매수해야 하는 사람의 최솟값 출력

## 풀이
1. 큰순으로 정렬

2. 앞에 있는 값과 비교
- 다솜이의 표가 더 작을 경우, 다솜이의 표가 더 많을 때 까지 보충

3. 다시 크기 비교하기
"""
import sys

input = sys.stdin.readline

n = int(input())

votes = []

for _ in range(n):
    votes.append(int(input()))

# 기호 1번 : 다솜이
dasom = votes.pop(0)

# 처음 값

# 만약 다솜이만 나왔거나 현재 다솜이가 가장 많은 득표율을 받았을 때
if n == 1 or dasom > max(votes):
    print(0)
    exit(0)

ans = 0

while True:
    if dasom <= max(votes):
        ans += 1
        votes[votes.index(max(votes))] -= 1
        dasom += 1
    else:
        break

print(ans)