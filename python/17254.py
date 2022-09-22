keyboard_num, typing = map(int, input().split())

a = list(range(1, keyboard_num+1))
data = [list(input().split()) for i in range(typing)]

for i in range(typing):
    data[i][0] = int(data[i][0])
    data[i][1] = int(data[i][1])

data.sort(key=lambda x:(x[1], x[0]))

for i in range(typing):
    print(data[i][2], end='')