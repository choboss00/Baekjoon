import sys

INPUT = sys.stdin.readline().strip().upper()

dic = {}

for chr in INPUT:
    if chr in dic:
        dic[chr] += 1
    else:
        dic[chr] = 1

dic2 = sorted(dic.items(), key=lambda x: x[1])
#value 값이 같으면 물음표 출력, 아니면 정상적으로 출력

max = dic2[len(dic2)-1][1]
for i in range(0, len(dic2)):
    if(max == 1):
        print(dic2[len(dic2)-1][0])
        break
    if (max == dic2[len(dic2)-2-i][1]):
        print("?")
        break
    else:
        print(dic2[len(dic2)-1][0])
        break