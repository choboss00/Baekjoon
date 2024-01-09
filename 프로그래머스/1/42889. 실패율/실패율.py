from collections import deque

def solution(N, stages):
    answer = []
    
    # 정렬
    stages.sort()
    # 덱으로 변환
    stages = deque(stages)
    
    for i in range(1, N+1):
        # 분자 계산
        a = 0
        while stages:
            n = stages.popleft() # 뽑은 원소
            # 더 작은 원소일 경우
            if n < i:
                continue
            elif n == i: # 분자
                a += 1
            else:
                stages.appendleft(n)
                break
                # 종료
        # 분모 계산
        b = len(stages)
        
        if a == 0: # 스테이지에 도달한 유저가 없는경우
            answer.append([i, 0])
        else:
            answer.append([i, a/(a+b)])
    
    answer.sort(key=lambda x : (-x[1], x[0]))
    
    ans = []
    
    for key, value in answer:
        ans.append(key)
    
    return ans

"""
## 실패율

## 문제
1. 실패율을 구하는 코드를 완성하기

2. 실패율 = 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수

3. 전체 스테이지의 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages

4. 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열 return 하기

## 제한사항
1. N : 1 이상 500 이하의 자연수

2. stages : 1 이상 20만 이하

3. stages : 1 이상 N+1 이하의 자연수
- 각 자연수는 사용자가 현재 도전 중인 스테이지의 번호
- N+1 : 마지막 스테이지까지 클리어한 사용자

4. 실패율이 같은 스테이지가 있을 경우, 작은 번호의 스테이지가 먼저 오도록 해야 함 ( 정렬 )

5. 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0
- divide by zero 예외처리 체크해줄 필요가 있음

## 풀이
1. 예시를 따라가며 풀이
- N : 5 ( 5 스테이지 )
- 8명의 사용자 ( len(stages) )
- 1 스테이지 = 1/8 ( 1명의 사용자가 도전중 / 이미 클리어한 사용자 수)
... 반복

2. 풀이 일반화
- 현재 단계보다 작은 경우 -> 제외
- 현재 단계와 같은 경우 -> 분자 ( 도전중 )
- 현재 단계보다 값이 큰 경우 -> 분모 ( 클리어 )
- 실패율이 높은 순으로 정렬 (1), 실패율이 같은 경우 스테이지가 작은 순으로 정렬 (2)
"""