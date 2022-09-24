import sys
import math
def isPrime(a):
    if (a < 2):
        return False
    for i in range(2, int(math.sqrt(a))+1):
        if(a % i == 0):
            return False
    return True
# 숫자 받기
M, N = map(int, sys.stdin.readline().split())
# 소수 찾기 프로그램
num = 0
for i in range(M, N+1):
    if (isPrime(i)):
        print(i)