def solution(storey):
    answer = 0
    
    while storey > 0:
        storey, rem = divmod(storey, 10)
        
        if rem > 5 or (rem == 5 and storey % 10 >= 5):
            answer += (10 - rem)
            storey += 1
        else:
            answer += rem
        
    return answer

"""
## 마법의 엘리베이터 : Level 2

## 문제
1. 버튼 : -100, -10, -1, 1, 10, 100 처럼 절댓값이 10^c 형태인 정수들이 적힌 버튼이 있음

2. 버튼을 누르면 현재 층 수에 적혀있는 값에 더해줌
- 단, 결괏값이 0 보다 작으면 움직이지 않음 ( 음수 체크 )

3. 최소한의 버튼을 눌러서 0층으로 내려가는 함수 작성하기

## 풀이
1. bfs 탐색 ( 시간 초과 )

2. 그리디하게 접근
"""