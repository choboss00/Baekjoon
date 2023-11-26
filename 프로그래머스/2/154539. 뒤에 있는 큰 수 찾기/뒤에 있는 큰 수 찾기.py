def solution(numbers):
    answer = []
    
    stack = []
    
    while numbers:
        now = numbers.pop()
        
        if len(answer) == 0:
            answer.append(-1)
            stack.append(now)
        else:
            if stack[-1] > now:
                answer.append(stack[-1])
                stack.append(now)
            else:
                while stack:
                    check = stack.pop()
                    
                    if check > now:
                        answer.append(check)
                        stack.append(check)
                        stack.append(now)
                        break
                
                if len(stack) == 0:
                    answer.append(-1)
                    stack.append(now)
    
    answer.reverse()
    
    return answer

"""
1. 정수로 이루어진 배열 numbers
2. 배열의 각 원소들에 대해 자신보다 뒤에 있는 숫자 중에서 자신보다 크면서
가장 가까이 있는 수를 뒷 큰수라고 함
3. 모든 원소에 대한 뒷 큰수들을 차례로 담은 배열 return 하기

풀이
1. 뒤에서부터 담으면서 최댓값 갱신해주기
"""