def solution(arr1, arr2):
    answer = []
    
    # 행렬의 행, 열 길이
    x1, y1, x2, y2 = len(arr1[0]), len(arr1), len(arr2[0]), len(arr2)
    
    for i in range(y1):
        ans_list = []
        for j in range(x2):
            num = 0
            for k in range(x1):
                num += (arr1[i][k] * arr2[k][j])
            ans_list.append(num)
        answer.append(ans_list)
        
    
    
    return answer

"""
## 행렬의 곱셈

## 문제
1. 2차원 행렬 2개를 입력받아 곱한 결과를 반환하는 함수 만들기

## 제한 조건
1. 행과 열의 길이 : 2 이상 100 이하

2. 원소 : -10 이상 20 이하의 자연수

3. 곱할 수 있는 배열만 주어짐 ( 예외처리 할 필요 없음 )

## 풀이
1. 문제 조건에 맞게 풀이 ( 행렬 곱 )
"""