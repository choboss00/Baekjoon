import math

def solution(r1, r2):
    answer = 0
    # 한쪽 사분면만 먼저 계산
    for i in range(1, r2+1):
        max_y = int((r2 ** 2 - i ** 2) ** 0.5)
        if i < r1:
            min_y = math.ceil((r1 ** 2 - i ** 2) ** 0.5)
        else:
            min_y = 0
        answer = (answer + max_y - min_y + 1)
    
    return answer * 4

"""
1. 점과 원점사이의 거리를 구한 뒤, 그 점이 원 두개 사이에 있는지 체크
2. 한 사분면에서 점들을 다 구한 뒤, * 4
"""