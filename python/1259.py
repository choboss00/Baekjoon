import sys

list = []
while(True):
    ex = sys.stdin.readline().strip()
    list.append(ex)
    if(list[len(list)-1] == '0'):
        break

del list[len(list)-1]

for i in range(0, len(list)):
    check_list = []
    for j in range(0 ,len(list[i])):
        if(list[i][j] == list[i][len(list[i])-1-j]):
            check_list.append("yes")
        else:
            check_list.append("no")
    if "no" in check_list:
        print("no")
    else:
        print("yes")


