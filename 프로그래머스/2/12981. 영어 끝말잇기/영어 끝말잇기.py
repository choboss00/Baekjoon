import math

def solution(n, words):
    idx = 0
    s = ''
    s_set = set()
    
    for i in range(len(words)):
        if i == 0: # 첫번째
            s = words[i][-1]
            idx += 1
            s_set.add(words[i])
            continue
            
        if s == words[i][0]:
            if words[i] in s_set:
                return [idx+1, math.ceil((i+1) / n)]
            idx = (idx + 1) % n
            s = words[i][-1]
            s_set.add(words[i])
        else:
            return [idx+1, math.ceil((i+1) / n)]
    return [0,0]

"""
## 영어 끝말잇기

## 문제
1. 1부터 n까지 번호가 붙어있는 n명의 사람이 영어 끝말잇기를 하고 있음

2. 영어 끝말잇기는 다음과 같은 규칙으로 진행됨
- 1번부터 번호 순서대로 한 사람씩 차례대로 단어를 말함
- 마지막 사람이 단어를 말한 다음에는 다시 1번부터 시작함
- 앞사람이 말한 단어의 마지막 문자로 시작하는 단어를 말해야함
- 이전에 등장했던 단어는 사용할 수 없음
- 한 글자인 단어는 인정되지 않음

3. 사람의 수 n과 사람들이 순서대로 말한 단어 words 가 매개변수로 주어짐

4. 가장 먼저 탈락하는 사람의 번호와 그 사람이 자신의 몇 번째 차례에 탈락하는지를 구해서 return 하는 solution 함수 작성하기
- 정답은 [번호, 차례] 형태
- 만약 주어진 단어들로 탈락자가 생기지 않는다면, [0, 0] return 하기
"""
