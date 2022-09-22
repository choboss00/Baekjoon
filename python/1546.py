num = int(input())
data = list(map(int, input().split()))

result = 0

for i in range(0, num):
    for j in range (i, num - 1):
        tmp = data[j]
        data[j] = data[j+1]
        data[j+1] = tmp

for i in range(0, num):
    result += float((data[i]/max(data)) * 100)

print(result/num)


#while (data[j] > data[j + 1]):
#    tmp = data[j]
#    data[j] = data[j + 1]
#    data[j + 1] = tmp
#    j -= 1