
num = int(input())
i = 0
j = 1
result = []
result2 = []

data = [list(map(int, input().split())) for i in range(num)]

for i in range(0, num):
    sum = 0
    for j in range(0, data[i][0]):
       sum += data[i][j+1]
    result.append(sum/float(data[i][0]))

for i in range(0, num):
    count = 0
    for j in range(0, data[i][0]):
        if (result[i] < data[i][j+1]):
            count += 1

    result2.append((float(count)/data[i][0]) * 100)

for i in range(0, num):
    print('%.3f%%' %result2[i])

