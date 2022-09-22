import sys

def Euclid(a, b):
    if(b==0):
        return a
    return Euclid(b, a % b)

x, y = map(int, sys.stdin.readline().split())

res_1 = Euclid(x, y)

print(res_1)
print(int(x*y/res_1))

# 최대공약수 : 유클리드 호제법
# 최소공배수 : x * y / 최대공약수