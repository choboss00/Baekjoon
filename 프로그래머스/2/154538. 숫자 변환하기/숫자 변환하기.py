from collections import deque

def solution(x, y, n):
    answer = -1
    
    queue = deque()
    
    queue.append([y, 0]) # 현재 값, 횟수
    
    while queue:
        now, time = queue.popleft()
        
        if now == x:
            return time
        elif now < x:
            continue
        else:
            queue.append([now - n, time + 1])
            if now % 2 == 0:
                queue.append([now // 2, time + 1])
            if now % 3 == 0:
                queue.append([now // 3, time + 1])
    
    
    
    return answer

"""
1. 자연수 x 를 y 로 변환
2. 사용할 수 있는 연산
- x 에 n 더하기
- x 에 2 곱하기
- x 에 3 곱하기
3. 자연수 x, y, n 이 매개변수로 주어질 때, x 를 y 로 변환하기 위해 필요한 최소 연산 횟수 return 하기
- x 를 y 로 만들 수 없다면 -1 return 하기

풀이 : bfs 탐색 진행
"""