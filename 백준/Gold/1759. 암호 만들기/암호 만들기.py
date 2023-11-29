"""
1759번 : 암호 만들기
1. 새로운 보안 시스템 : 암호로 동작
2. 암호 : 서로 다른 L개의 알파벳 소문자들로 구성됨
- 최소 1개의 모음 ( a, e, i, o, u ) 과 최소 2개의 자음으로 구성
- 오름차순 정렬
3. 암호로 사용했을 법한 문자의 종류 : C가지
- 이 알파벳을 입수한 상태 ( c개의 문자 )
- 가능성 있는 암호들을 모두 구하는 프로그램 작성하기

입력
1. 두 정수 L, C
- L : 암호 문자열의 길이
- C : 문자들의 갯수

출력
1. 사전식으로 가능성있는 암호 모두 출력하기

풀이
1. 백트래킹
- 자음의 갯수, 모음의 갯수 체크하면서 진행
- 자음의 갯수 >= 2, 모음의 갯수 >= 1 일 때 출력 리스트에 담기
"""
import sys

def back(ans, depth, level, g1, g2):
    if len(ans) == depth and g1 >= 1 and g2 >= 2:
        ans_list.append(ans)
        return

    for i in range(level, C):
        ans = ans + c_list[i]
        # 현재 모음일 경우
        check = False
        if c_list[i] in ['a', 'e', 'i', 'o', 'u']:
            g1 += 1
            check = True
        else:
            g2 += 1
        back(ans, depth, i+1, g1, g2)
        ans = ans[:len(ans)-1]
        if check == True:
            g1 -= 1
        else:
            g2 -= 1
input = sys.stdin.readline
# L : 문자열 길이, C : 문자 수
L, C = map(int, input().split())

c_list = input().strip().split()
# 오름차순 정렬
c_list.sort()
# 출력 결과물을 담을 리스트
ans_list = []
# 출력 결과
ans = ''
# 백트래킹 진행하기 ( 문자열, 깊이, 레벨, 자음의 수, 모음의 수 )
back(ans, L, 0, 0, 0)

for a in ans_list:
    print(a)
