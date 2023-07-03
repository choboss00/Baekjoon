"""
28278번. 스택 2 ( 실버 4 )

정수를 저장하는 스택 구현 후 명령 처리 프로그램 작성하기
"""
import sys

input = sys.stdin.readline

n = int(input())
stack = []

for i in range(n):
    n_list = list(map(int, input().split()))
    # 만약 리스트의 길이가 1보다 크면 삽입
    if len(n_list) > 1:
        stack.append(n_list[-1])
    else:
        if n_list[0] == 2:
            if len(stack) == 0:
                print(-1)
            else:
                print(stack.pop())
        elif n_list[0] == 3:
            print(len(stack))
        elif n_list[0] == 4:
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        elif n_list[0] == 5:
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[-1])
