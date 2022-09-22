import sys

count = 0
N = int(sys.stdin.readline())

list = [0 for i in range(N)]

for i in range(N):
    list[i] = sys.stdin.readline().split()
    list[i][0] = int(list[i][0])
    list[i].append(count)
    count += 1

list.sort(key=lambda x:(x[0],x[2]))

for i in list:
    del i[2]
    print("%d %s" % (i[0], i[1]))

