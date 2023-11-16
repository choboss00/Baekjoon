def solution(survey, choices):
    answer = ''
    ans_list = [0 for _ in range(8)]
    # survey list 의 길이
    surLen = len(survey)
    for i in range(surLen):
        # 점수 구하기
        cnt = 0
        if choices[i] == 1:
            cnt = 3
        elif choices[i] == 2:
            cnt = 2
        elif choices[i] == 3:
            cnt = 1
        elif choices[i] == 4:
            cnt = 0
        elif choices[i] == 5:
            cnt = -1
        elif choices[i] == 6:
            cnt = -2
        elif choices[i] == 7:
            cnt = -3
        # 라이언, 튜브
        if 'R' in survey[i]:
            # 라이언일 경우
            if survey[i][0] == 'R':
                # 첫번째 원소에 값 넣기
                ans_list[0] += cnt
            elif survey[i][0] == 'T':
                ans_list[1] += cnt
        elif 'C' in survey[i]:
            # 콘, 프로도
            if survey[i][0] == 'C':
                ans_list[2] += cnt
            else:
                ans_list[3] += cnt
        elif 'J' in survey[i]:
            if survey[i][0] == 'J':
                ans_list[4] += cnt
            else:
                ans_list[5] += cnt
        elif 'A' in survey[i]:
            if survey[i][0] == 'A':
                ans_list[6] += cnt
            else:
                ans_list[7] += cnt
    
    max1 = max(ans_list[0], ans_list[1])
    max2 = max(ans_list[2], ans_list[3])
    max3 = max(ans_list[4], ans_list[5])
    max4 = max(ans_list[6], ans_list[7])
    
    if max1 == ans_list[0] and max1 == ans_list[1]:
        answer = answer + 'R'
    else:
        if max1 == ans_list[0]:
            answer = answer + 'R'
        else:
            answer = answer + 'T'
    
    if max2 == ans_list[2] and max2 == ans_list[3]:
        answer = answer + 'C'
    else:
        if max2 == ans_list[2]:
            answer = answer + 'C'
        else:
            answer = answer + 'F'
    
    if max3 == ans_list[4] and max3 == ans_list[5]:
        answer = answer + 'J'
    else:
        if max3 == ans_list[4]:
            answer = answer + 'J'
        else:
            answer = answer + 'M'
    
    if max4 == ans_list[6] and max4 == ans_list[7]:
        answer = answer + 'A'
    else:
        if max4 == ans_list[6]:
            answer = answer + 'A'
        else:
            answer = answer + 'N'
    
    
    return answer


"""
1. 나만의 성격 유형 검사지 만들기
2. 4개 지표로 성격 유형을 구분함
- 1번 지표 : R 라이언, T 튜브
- 2번 지표 : C 콘, F 프로도
- 3번 지표 : J 제이지, M 무지
- 4번 지표 : A 어피치, N 네오
3. 검사지 : N 개의 질문이 있고, 각 질문당 7개의 선택지가 존재함
- 매우 동의 / 매우 비동의 : 3점
- 동의 / 비동의 : 2점
- 약간 동의 / 약간 비동의 : 1점
- 모르겠음 : 0점
4. 검사 결과 : 모든 질문의 성격 유형 점수를 더하여 각 지표에서 더 높은 점수를 받는 성격 유형이 검사자의 성격 유형이라고 판단함
- 점수가 같을 경우, 두 성격 유형 중 사전순으로 빠른 성격 유형을 검사자의 성격 유형이라 판단

풀이
1. 리스트 원소를 하나씩 받으면서 검사하고, 점수 더하기
"""