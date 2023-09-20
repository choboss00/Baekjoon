import sys

input = sys.stdin.readline

n,m = input().strip().split()

n_set = set()

for i in range(int(n)):
    n_set.add(input().strip())

if m == 'Y':
    print(len(n_set))
elif m == 'F':
    print(len(n_set) // 2)
elif m == 'O':
    print(len(n_set) // 3)