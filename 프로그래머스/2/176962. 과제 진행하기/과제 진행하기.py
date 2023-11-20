def solution(plans):
    answer = []
    
    plans.sort(key=lambda x : x[1])
    
    # stack
    stack = []
    
    for subject, start, time in plans:
        h, m = map(int, start.split(':'))
        start = 60*h+m
        time = int(time)

        if stack:
            prev_subject, prev_start, prev_time = stack.pop()
            # 이전 시작시간과 현재 시작시간 비교
            extra_time = start - prev_start
            # 현재 시간안에 처리할 수 없는 경우
            if extra_time < prev_time:
                stack.append((prev_subject, prev_start, prev_time-extra_time))
            else:
                answer.append(prev_subject)
                # 남은 시간
                extra_time = extra_time - prev_time

                while stack and extra_time :
                    prev_subject, prev_start, prev_time = stack.pop()

                    if extra_time < prev_time:
                        stack.append((prev_subject, prev_start, prev_time-extra_time))
                        break
                    else:
                        answer.append(prev_subject)
                        extra_time = extra_time - prev_time

        stack.append((subject, start, time))
    
    while stack:
        s = stack.pop()
        answer.append(s[0])
    
    return answer

"""
1. 과제는 시작하기로 한 시각이 되면 시작함
2. 새로운 과제를 시작할 시각 -> 기존 과제는 멈추고 새로운 과제 시작
3. 진행중이던 과제를 끝냈을 때, 잠시 멈춘 과제 o -> 멈춰둔 과제 이어서 진행
- 과제를 끝낸 시각에 새로 시작하는 과제와 잠시 멈춰둔 과제 둘다 존재할 경우
- 새로 시작해야하는 과제부터 진행
4. 멈춰둔 과제가 여러개 -> 가장 최근에 멈춘 과제부터 시작하기

풀이 : 스택
"""