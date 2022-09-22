from fractions import Fraction
import sys

N = int(sys.stdin.readline())
list = list(map(int, sys.stdin.readline().split()))

num_list = []
for i in range(N-1):
        num_list.append(Fraction(list[0], 1) / Fraction(list[i+1], 1))
        print("%d/%d" %(num_list[i].numerator, num_list[i].denominator))