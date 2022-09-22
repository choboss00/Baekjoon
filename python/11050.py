import sys

x, y = map(int, sys.stdin.readline().split())
x_num = 1
y_num = 1
for i in range(y):
    x_num *= x
    y_num *= y
    x -= 1
    y -= 1

print(int(x_num / y_num))