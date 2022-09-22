import sys

N = int(sys.stdin.readline())

list = [0 for i in range(N)]
for i in range(N):
    list[i] = sys.stdin.readline().strip()

list.sort()
list.sort(key=lambda i:len(i))
new_list = []

for i in list:
    if i not in new_list:
        new_list.append(i)

for i in new_list:
    print(i)