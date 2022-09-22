N = int(input())
list = [list(map(int, input().split())) for i in range(0,N)]


for i in list:
    count = 1
    for j in list:
        if(i[0] < j[0] and i[1] < j[1]):
            count += 1
    print(count, end=' ')


# 자기보다 큰값이 몇개있는지에 따라 값 출력
# for문에서 2차원 리스트 넣을때 어떻게 들어가는지 생각