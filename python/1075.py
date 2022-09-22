N = int(input())
F = int(input())

N_str = str(N)
N_int = int(N_str[0:len(N_str)-2] + '00')

result = N_int % F

while(True):
    if(result == 0):
        break
    else:
        N_int += 1
        result = N_int % F

n1 = N_int

for i in range(1, 10):
    if(n1 == i):
        print("0%d" %(n1))

str_N = str(n1)
print(str_N[-2:])




