N = int(input())

list = [list(map(int, input().split())) for i in range(N)]

list.sort(key=lambda x:(x[1], x[0]) )


for i in range(N):
        print("%d %d" %(list[i][0], list[i][1]))