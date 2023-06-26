import sys

"""
전공평점 계산기 만들기
전공 평점 : 학점 * 과목평점 / 학점의 총합

입력 : 20줄
"""

input = sys.stdin.readline

# 합 구하기
num1 = 0
num_sum = 0
for i in range(20):
    split_list = input().split()
    # 과목 학점
    m = float(split_list[1])
    # 과목평점
    s = 0
    # 학점 * 과목평점
    if split_list[2] == 'A+':
        s = 4.5
    elif split_list[2] == 'A0':
        s = 4.0
    elif split_list[2] == 'B+':
        s = 3.5
    elif split_list[2] == 'B0':
        s = 3.0
    elif split_list[2] == 'C+':
        s = 2.5
    elif split_list[2] == 'C0':
        s = 2.0
    elif split_list[2] == 'D+':
        s = 1.5
    elif split_list[2] == 'D0':
        s = 1.0
    elif split_list[2] == 'F':
        s = 0
    elif split_list[2] == 'P':
        s = 'pass'

    if s != 'pass':
        num_sum += m
        num1 += s * m

print(round(num1 / num_sum, 6))
