def solution(prices):
    answer = []
    
    stack = []
    
    while prices:
        # 가장 마지막 원소 pop
        p = prices.pop()
        
        if len(answer) == 0: # 아무 원소도 들어있지 않을 경우 ( 가장 마지막 )
            answer.append(0)
            stack.append(p)
        elif len(answer) == 1: # 원소가 하나밖에 없을 경우
            answer.append(1)
            stack.append(p)
        else:
            cnt = 1
            check = False
            # 스택의 마지막부터 비교
            for i in range(len(stack)-1, -1, -1):
                if p <= stack[i]:
                    cnt += 1
                else:
                    answer.append(cnt)
                    check = True
                    break
            # 마지막까지 stack 을 반복했을경우
            if not check:
                answer.append(cnt-1)
            
            stack.append(p)
            
    answer.reverse()
    
    return answer

"""
## 주식 가격

## 문제
1. 초 단위로 기록된 주식 가격이 담긴 배열

2. 가격이 떨어지지 않은 기간은 몇 초인지 return 하는 함수 만들기

## 풀이
1. prices 뒤에서 접근

2. 
"""