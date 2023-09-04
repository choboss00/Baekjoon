import sys

input = sys.stdin.readline

while True:
    try:
        s = int(input())
        # 자릿수
        i = 0
        ans = 0
        while True:
            i += 1
            ans = 10 * ans + 1
    
            if ans % s == 0:
                print(i)
                break
    except:
        break