from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    # 각 큐당 구해야 할 값
    queSum = ( sum(queue1) + sum(queue2) )
    
    if queSum % 2 == 1:
        return -1
    else:
        queSum = queSum // 2
    
    queLen = len(queue1) + len(queue2)
    q1Sum = sum(queue1)
    q2Sum = sum(queue2)
    
    # 반복할 횟수
    cnt = 0
    
    while q1Sum != q2Sum:
        # 예외 처리
        if cnt >= queLen:
            return -1
        # queue1 이 더 클경우
        while queue1 and q1Sum > q2Sum:
            q1 = queue1.popleft()
            queue2.append(q1)
            q1Sum -= q1
            q2Sum += q1
            cnt += 1
        while queue2 and q2Sum > q1Sum:
            q2 = queue2.popleft()
            queue1.append(q2)
            q1Sum += q2
            q2Sum -= q2
            cnt += 1
        
    return cnt

"""
1. 길이가 다른 두 개의 큐
2. 하나의 큐를 골라 pop -> 다른 큐에 append
- 각 큐 원소 합이 같도록 만들려고 함
- 이때 필요한 작업의 최소 횟수 구하기
- 1번의 pop + 1번의 append = 1회 수행
3. 두 큐의 원소의 합 구하기
- 절반으로 쪼갠 값이 각 큐에 들어가야 함

풀이
1. 크기가 큰 큐에서 먼저 pop -> 다른 큐에 append
2. 다시 크기 비교 후 같으면 종료
- 다르면 다시 크기가 큰 큐에서 pop
3. 쪼갤 수 없으면 -1 리턴하기
- 하나의 큐에서 pop 한 횟수가 큐의 길이보다 클 경우 -> -1 리턴
"""