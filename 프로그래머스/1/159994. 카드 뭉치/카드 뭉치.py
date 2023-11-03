from collections import deque

def solution(cards1, cards2, goal):
    c1, c2, g = deque(cards1), deque(cards2), deque(goal)
    
    while g:
        # 첫번째 문자
        goalStr = g.popleft()
        
        # 비교하기
        if len(c1) > 0 and c1[0] == goalStr:
            c1.popleft()
        elif len(c2) > 0 and c2[0] == goalStr:
            c2.popleft()
        # 없는 문자일 경우
        else:
            return "No"
    return "Yes"

"""
1. 영어 단어가 적힌 카드 뭉치 2개
2. 단어 배열 규칙
- 원하는 카드 뭉치에서 카드를 순서대로 한장씩 사용
- 한번 사용한 카드는 다시 사용할 수 없음
- 카드를 사용하지 않고 다음 카드로 넘어갈 수 없음
- 기존에 주어진 카드 뭉치의 단어 순서를 바꿀 수 없음
3. 단어를 만들 수 있을 때 -> Yes, 만들 수 없으면 -> No return 하기

풀이
1. 카드에서 하나씩 빼보고, goal 의 첫번째 단어와 같을 경우 -> 같이 pop 하기
2. 그렇지 않으면, 다시 집어넣기
3. deque 이용
"""