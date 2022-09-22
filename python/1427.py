N = int(input())

N_list = list(map(int, str(N)))

N_list.sort()
N_list.reverse()

for i in N_list:
    print(i, end='')