y, x = map(int, input().split())

data = []

for i in range(y):
    data.append(input())

list = []

for i in range(y - 7):
    for j in range(x - 7):
        count_W = 0
        count_B = 0
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if(k+l) % 2 == 0:
                    if(data[k][l] != 'W'):
                        count_W += 1
                    if(data[k][l] != 'B'):
                        count_B += 1
                else:
                    if (data[k][l] != 'W'):
                        count_B += 1
                    if (data[k][l] != 'B'):
                        count_W += 1
        list.append(count_W)
        list.append(count_B)

print(min(list))