import sys

num_list = list(map(int, sys.stdin.readline().split()))
check_list = [1, 2, 3, 4, 5, 6, 7, 8]


if(num_list == check_list):
    print("ascending")
elif(num_list == list(reversed(check_list))):
    print("descending")
else:
    print("mixed")