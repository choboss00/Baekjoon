def solution(keymap, targets):
    answer = []
    
    for target in targets:
        ans_list = []
        for t in target:
            # target 의 문자에 맞는 값들이 있는지 돌기
            cnt_list = []
            for key in range(len(keymap)):
                i = keymap[key].index(t) if t in keymap[key] else None
                
                if i == None:
                    cnt_list.append(101)
                else:
                    cnt_list.append(i+1)
            
            # 만약 101 이 min 값 일 경우
            minCnt = min(cnt_list)
            if minCnt == 101:
                ans_list.append(-1)
            else:
                ans_list.append(minCnt)
        # 만약 -1 이 존재할 경우
        if -1 in ans_list:
            answer.append(-1)
        else:
            answer.append(sum(ans_list))
    return answer


# 하나의 키에 여러개의 문자가 할당될 수 있음
# 키 하나에 여러 문자가 할당된 경우, 동일한 키를 연속해서 빠르게 누르면 할당된 순서대로 문자가 바뀜
# 휴대폰 자판의 키 갯수 : 1 ~ 100
# 입력 문자 : 무작위 배열, 같은 문자가 자판 전체에 여러번 o, 키 하나에 같은 문자가 여러번 o
# 특정 문자열을 작성할 때, 키를 최소 몇번 눌러야 그 문자열을 작성할 수 있는지 알아보기
# 출력 못하면 -1 출력하기
# 리스트 돌면서 키를 몇번눌러야하는지 탐색하기 ( 브루트포스 ) -> 가장 적은 값 추가하기
# 인덱스 번호를 뽑아내기 ( 어차피 가장 앞에껄 누르니 )