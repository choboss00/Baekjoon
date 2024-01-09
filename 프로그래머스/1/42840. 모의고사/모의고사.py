def solution(answers):
    answer = []
    
    po_one = [1,2,3,4,5]
    po_two = [2,1,2,3,2,4,2,5]
    po_three = [3,3,1,1,2,2,4,4,5,5]
    
    arr = [0] * 3
    for i in range(len(answers)):
        if po_one[(i % 5)] == answers[i]:
            arr[0] += 1
        
        if po_two[(i % 8)] == answers[i]:
            arr[1] += 1
        
        if po_three[(i % 10)] == answers[i]:
            arr[2] += 1
    
    # 배열중 가장 큰 값 찾기
    max_num = max(arr)
    
    for i in range(3):
        if max_num == arr[i]:
            answer.append(i+1)
        
    return answer

"""
## 모의고사

## 문제
1. 1번 문제부터 마지막 문제까지 다음과 같은 방식으로 찍으려고 함
- 1번 수포자 -> 순차적으로 탐색
- 2번 수포자 -> 홀수번째 배열을 탐색할때마다 2 탐색, 나머지 짝수는 1, 3, 4, 5 탐색
- 3번 수포자 -> 3 2개, 1 2개, 2 2개, 4 2개, 5 2개 순으로 탐색

2. 1번 ~ 마지막 문제까지의 정답이 순서대로 들은 배열이 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하기

## 제한 조건
1. 시험 : 최대 10000문제

2. 문제의 답 : 1, 2, 3, 4, 5 중 하나

3. 가장 높은 점수를 받은 사람이 여럿일 경우, 오름차순 정렬하기

## 풀이
1. 패턴 파악
"""