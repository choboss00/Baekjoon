import sys

input = sys.stdin.readline

n = int(input())

if n < 10:
    print(n)
elif n < 100:
    n -= 9
    print(9 + n * 2)
elif n < 1000:
    n -= 99
    print(189 + n * 3)
elif n < 10000:
    n -= 999
    print(2889 + n * 4)
elif n < 100000:
    n -= 9999
    print(38889 + n * 5)
elif n < 1000000:
    n -= 99999
    print(488889 + n * 6)
elif n < 10000000:
    n -= 999999
    print(5888889 + n * 7)
elif n < 100000000:
    n -= 9999999
    print(68888889 + n * 8)
elif n == 100000000:
    print(788888889 + 9)