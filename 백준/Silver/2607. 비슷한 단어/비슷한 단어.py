import sys
import copy

input = sys.stdin.readline

n = int(input())

str_list = [input().strip() for _ in range(n)]

# 첫번째 단어
check_str = list(str_list[0])
firstLen = len(check_str)

# 정답
ans = 0
for i in range(1, n):
    copy_str = copy.deepcopy(check_str)
    sub_str = list(str_list[i])
    cnt = 0

    for i in sub_str:
        if i in copy_str:
            copy_str.remove(i)
        else:
            cnt += 1
            
    if cnt <= 1 and len(copy_str) <= 1:
       ans += 1

print(ans)