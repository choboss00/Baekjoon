import sys

input = sys.stdin.readline

fn = input().strip()
sn = input().strip()

stack = []
for i in fn:
    # 문자열 담기
    stack.append(i)
    check_str = ''
    # 만약 현재 담은 문자와 끝값이 같을 경우
    if len(stack) >= len(sn):
        if stack[-1] == sn[-1]:
            check_str = stack[-1]
            check = -2
            while abs(check) != len(sn)+1:
                if stack[check] == sn[check]:
                    check_str = stack[check] + check_str
                check -= 1
        if check_str == sn:
            for i in range(len(sn)):
                stack.pop()
                
if len(stack) == 0:
    print('FRULA')
else:
    print(''.join(stack))