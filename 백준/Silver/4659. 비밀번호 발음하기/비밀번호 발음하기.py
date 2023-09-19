import sys

input = sys.stdin.readline

while True:
    s = input().strip()

    if s == 'end':
        break

    # 모음을 체크하는 카운트
    cnt = 0

    # 모음 혹은 자음이 연속으로 오는지 체크하는 카운트
    cnt1, cnt2 = 0, 0

    # 같은 글자가 연속으로 두번오는지 체크
    stack = ''

    check = True

    for i in s:
        # 현재 글자가 모음일 경우
        if i in ['a', 'e', 'i', 'o', 'u']:
            cnt += 1
            cnt1 += 1
            cnt2 = 0
        else:
            cnt2 += 1
            cnt1 = 0
        # 자음 혹은 모음이 3개 연속으로 오면 안됨
        if cnt1 >= 3 or cnt2 >= 3:
            print(f'<{s}> is not acceptable.')
            check = False
            break
        # 같은 글자가 연속으로 오는 경우
        if len(stack) > 0:
            if stack[-1] == i:
                if i == 'e' or i == 'o':
                    stack = stack + i
                else:
                    print(f'<{s}> is not acceptable.')
                    check = False
                    break
            # 다른 문자가 올 경우
            else:
                stack = stack + i
        else:
            stack = stack + i

    if check:
        if cnt > 0:
            print(f'<{s}> is acceptable.')
        else:
            print(f'<{s}> is not acceptable.')