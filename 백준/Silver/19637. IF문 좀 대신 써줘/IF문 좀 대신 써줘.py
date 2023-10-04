import sys

input = sys.stdin.readline

n, m = map(int, input().split())

n_numList = []
n_strList = []
m_list = []
ans_list = []

for _ in range(n):
    s, num = input().split()
    # insert after type casting the variable
    n_numList.append(int(num))
    n_strList.append(s)

for _ in range(m):
    check_num = int(input())

    # index setting
    left, right = 0, n-1

    # string
    ans = ''

    while left <= right:
        mid = (left + right) // 2

        # check -> back
        if check_num <= n_numList[mid]:
            ans = n_strList[mid]
            right = mid - 1
        else:
            left = mid + 1

    ans_list.append(ans)

for i in ans_list:
    print(i)