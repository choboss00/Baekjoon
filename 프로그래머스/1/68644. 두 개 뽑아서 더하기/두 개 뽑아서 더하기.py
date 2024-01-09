def solution(numbers):
    answer = []
    
    # numbers 의 길이
    n = len(numbers)
    
    # 방문
    visited = [-1 for _ in range(201)]
    
    for i in range(n):
        for j in range(i+1, n):
            if visited[numbers[i] + numbers[j]] == -1: # 방문하지 않았을 때
                answer.append(numbers[i] + numbers[j])
                visited[numbers[i] + numbers[j]] = 1
    
    answer.sort()
    
    return answer

"""
## 두 개 뽑아서 더하기

## 문제
1. 정수 배열 numbers

2. 배열에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하기

## 제한사항
1. 배열의 길이 : 2 ~ 100

2. 배열의 모든 수 : 0 ~ 100

## 풀이
1. 서로 다른 인덱스에 있는 2개의 수를 뽑기
- 2중 반복문으로 탐색

2. 같은 수는 넣지 않아야 함
"""