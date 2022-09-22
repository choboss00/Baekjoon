count = 1

str = input()
list = list(str)

for i in range(0, len(list)):
    if(list[i] == ' '):
        count += 1

if(list[0] == ' '):
    count -= 1
if(list[-1] == ' '):
    count -= 1

print(count)