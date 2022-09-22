import sys

list = []

while(True):
    num = sys.stdin.readline().split()
    for i in range(len(num)):
        num[i] = int(num[i])
    num.sort()
    list.append(num)
    if(list[len(list)-1][0] == 0 and list[len(list)-1][1] == 0 and list[len(list)-1][2] == 0):
        break

del list[len(list)-1]

for i in range(0, len(list)):
    if(int(list[i][0]) != 0 and int(list[i][1]) != 0 and int(list[i][2]) != 0):
        if(int(list[i][0]) ** 2 + int(list[i][1]) ** 2 == int(list[i][2]) ** 2 ):
            print("right")
        else:
            print("wrong")
    else:
        print("wrong")
