import sys

N = int(sys.stdin.readline().strip())

arr = [0] * 10000

for i in range(N):
    num = int(sys.stdin.readline().strip())
    arr[num - 1] += 1

for i in range(10000):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i+1)
            
# 계수정렬 써서 푸는 문제