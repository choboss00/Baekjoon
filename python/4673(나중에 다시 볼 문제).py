i_num = set(range(1,10001))
j_num = set()

for i in range(1, len(i_num)):
    for j in str(i):
        i += int(j)
    j_num.add(i)

for i in sorted(i_num - j_num):
    print(i)

# 나중에 다시 풀어볼 문제