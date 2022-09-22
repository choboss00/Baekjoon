num = int(input())
data = [list(map(int, input().split())) for i in range(num)]

for i in range(num):
    num1 = data[i][0]
    num2 = data[i][1] % 4
    if (num2 % 4 == 0):
        num2 = 4
    result = (num1 ** num2)
    if (result % 10 == 0):
        print(10)
    else:
        print(result % 10)



