from collections import Counter

def solution(weights):
    answer = 0
    
    counter = Counter(weights)
    
    for i in counter:
        if counter[i] > 0:
            answer += counter[i] * (counter[i] - 1) // 2
            answer += counter[i] * counter[i * 2]
            answer += counter[i] * counter[i * 3 / 2]
            answer += counter[i] * counter[i * 4 / 3]

    
    return answer

"""
## 문제
1. 하나의 시소
- 중심으로부터 2, 3, 4거리의 지점에 좌석이 하나씩 존재

2. 시소 짝꿍 : 시소를 두명이 마주보고 탈 때, 시소가 평형인 상태에서 각각에 의해
시소에 걸리는 토크의 크기가 서로 상쇄되어 완전한 균형을 이루는 경우
- 즉 탑승한 사람의 무게와 시소 축과 좌석 간의 거리의 곱이 양쪽 다 같은 경우
- 즉 무게 * 시소 축과 좌석 간의 거리 가 양쪽이 동일해야 함

3. 사람들의 몸무게 목록이 주어질 때, 시소 짝꿍이 몇 쌍 존재하는지 구하기

## 첫번째 풀이 ( 시간초과 )
1. 몸무게 목록, [2,3,4] 를 활용해서 문제를 풀어야 함

2. 최소 공배수를 구하고, 나눈 값이 (1,1) 인 경우 -> 가능
- 나눈 값이 (1,2) 인 경우 -> 각각 2, 4 에 앉으면 되니 가능
- 나눈 값이 (2,3) 인 경우 -> 각각 2, 3 에 앉으면 되니 가능
- 나눈 값이 (3,4) 인 경우 -> 각각 3, 4 에 앉으면 되니 가능
- 나머지 경우 : 불가능

-> 2중 반복문의 경우, 시간초과 발생

## 2번째 풀이 ( 같은 몸무게 중복 처리 이슈때문에 실패 )
1. 리스트에 몸무게 값을 index 형태로 저장

2. 집합 객체로 변환 후 값 세기

-> 같은 몸무게가 여러 명일 경우 제대로 체크하지 못함

## 3번째 풀이 ( Counter 객체 활용 )


"""