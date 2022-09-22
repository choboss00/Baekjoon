result_list = []

for j in range(0, 3):
    num = int(input())
    sum = 0
    for i in range(0, num):
        res = int(input())
        sum += res
    if(sum == 0):
        result_list.append("0")
    elif(sum > 0):
        result_list.append("+")
    else:
        result_list.append("-")

print(result_list[0])
print(result_list[1])
print(result_list[2])