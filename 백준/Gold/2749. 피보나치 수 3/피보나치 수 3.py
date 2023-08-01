import sys

input = sys.stdin.readline

n = int(input())

l = [1,1]

while True:
    l.append((l[-1]+l[-2]) % 1000000)
    # 다시 1 1 로 돌아올 때
    if l[-2] == 1 and l[-1] == 1:
        break

# 1 1 로 돌아온 부분 제외
t = len(l) - 2
# 순서 맞추기
n = n % t
print(l[n-1])