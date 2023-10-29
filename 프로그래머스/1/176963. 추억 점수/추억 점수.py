def solution(name, yearning, photo):
    answer = []
    
    # dictionary 묶기
    photo_dict = dict()
    
    # name 과 yearning 의 길이가 같을 경우
    if len(name) == len(yearning):
        for i in range(len(name)):
            photo_dict[name[i]] = yearning[i]
    # 다를 경우
    else:
        sumYearning = sum(yearning) # 합한 값
        lenYearning = len(yearning) # 길이
        for i in range(lenYearning):
            photo_dict[name[i]] = yearning[i]
        # 나머지 이어서 채우기
        for j in range(lenYearning+1, len(name)):
            photo_dict[name[i]] = sumYearning
    
    # photo 에 맞는 점수 구하기
    for y in range(len(photo)):
        ansNum = 0
        for x in range(len(photo[y])):
            if photo[y][x] in photo_dict:
                ansNum += photo_dict[photo[y][x]]
        answer.append(ansNum)
        
    
    return answer

# 추억 점수 : 사진 속에 나오는 인물의 그리움 점수를 모두 합산한 값
# 그리움 점수가 없을 때 : 나머지 사람들의 그리움 점수를 합한 값
# 사람의 이름을 담은 문자열 배열 : name
# 그리움 점수를 담은 정수 배열 : yearning
# 사진에 찍힌 인물의 이름을 담은 이차원 문자열 배열 : photo
# 추억 점수를 photo 에 주어진 순서대로 배열에 담아 return 하는 함수 만들기
# dictionary 로 묶기 -> 만약 그리움점수가 없을 경우 : 합한 값이 대신 들어감