def solution(n,a,b):
    answer = 0
    
    while a != b:
        a = (a+1) // 2
        b = (b+1) // 2
        answer += 1

    return answer

"""
## 예상 대진표

## 문제
1. 대회 : N 명이 참가하고, 토너먼트 형시긍로 진행됨
- N 명의 참가자는 각각 1번부터 N번을 차례대로 배정받음
- 1 <-> 2, 3 <-> 4, ... N-1 <-> N번의 참가자끼리 게임을 진행함

2. 각 게임에서 이긴 사람은 다음 라운드에 진출할 수 있음
- 다음 라운드에 진출할 참가자의 번호는 다시 1번부터 N/2 번을 차례대로 배정받음

3. 게임은 최종 한명이 남을 때 까지 진행됨

4. 처음 라운드에서 A번을 가진 참가자는 경쟁자로 생각하는 B번 참가자와 몇번째 라운드에서 만나는지 궁금해졌음

5. 게임 참가자 수 N, 참가자 번호 A, 경쟁자 번호 B 가 함수 solution 의 매개변수로 주어짐
- 처음 라운드에서 A번을 가진 참가자는 경쟁자로 생각하는 B번 참가자와 몇 번째 라운드에서 만나는지 return 하는 함수 작성하기

6. A번 참가자와 B번 참가자는 서로 붙게 되기 전까지 항상 이긴다고 가정함

## 제한사항
1. N : 2^1 이상, 2^20 이하인 자연수
- 2의 지수승으루 주어지니 부전승은 발생하지 않음

2. A, B : N 이하인 자연수, ( A != B )

## 풀이
1. 예시
- N = 8, A = 4, B = 7
1라운드 : A 는 3번 참가자와 붙음, B 는 8번 참가자와 붙음
2라운드 : A 는 1번 참가자와 붙음, B 는 3번 참가자와 붙음
3라운드에서 만나게 되므로, 3을 return 하면 됨

"""
