from copy import deepcopy

def solution(want, number, discount):
    answer = 0
    
    want_dict = {}
    
    for i in range(len(want)):
        want_dict[want[i]] = number[i] # 초기화
    
    idx, last_idx = 0, len(discount)
    # 물건의 개수가 14개 일경우, idx 는 4까지 가야함
    while idx <= last_idx - 10:
        discount_sub_list = discount[idx:10+idx]
        # copy
        want_copy_dict = deepcopy(want_dict)
        
        for d in discount_sub_list:
            if d in want_copy_dict and want_copy_dict[d] > 0:
                want_copy_dict[d] -= 1
            else:
                break
        
        if sum(want_copy_dict.values()) == 0:
            answer += 1
        
        idx += 1
        
        
    
    
    return answer

"""
## 문제
1. 일정 금액 지불시 10일동안 회원 자격 부여

2. 회원을 대상으로 매일 1가지 제품을 할인하는 행사를 진행함

3. 할인하는 제품은 하루에 1개씩만 구매할 수 있음

4. 자신이 원하는 제품과 수량이 할인하는 날짜와 10일 연속으로 일치할 경우에 맞춰서 회원가입을 진행하려고 함
- 말그대로 할인하는 제품과 자신이 원하는 제품이 10일 연속으로 겹쳐야 함

5. 예시
- 원하는 제품 : 바나나 3, 사과 2, 쌀 2, 돼지고기 2, 냄비 1
- 할인하는 제품 : 치킨, 사과, 사과, ...

- 셋째 날부터 10일간 원하는 제품과 할인하는 제품의 수량이 일치하기 때문에 셋째 날, 넷째 날, 다섯째 날 중 하루에 회원가입을 하려고 함

6. 원하는 제품을 나타내는 문자열 배열 want

7. 원하는 제품의 수량을 나타내는 정수 배열 number

8. 마트에서 할인하는 제품을 나타내는 문자열 배열 discount

9. 원하는 제품을 모두 할인받을 수 있는 회원등록 날짜의 총 일수를 return 하는 함수 작성하기
- 가능한 날이 없다면 0 return 하기

## 입력
1. want : 원하는 제품

2. number : 원하는 제품의 수량

3. discount : 할인하는 제품 목록

## 출력
1. 원하는 제품을 모두 할인받을 수 있는 회원등록 날짜의 총 일수

## 풀이
1. 딕셔너리 활용

2. want, number 를 활용한 딕셔너리 만들기

3. discount 문자열을 key 로 바꾸기
"""