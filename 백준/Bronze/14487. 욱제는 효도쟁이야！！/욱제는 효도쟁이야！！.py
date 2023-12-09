import sys

input = sys.stdin.readline

n = int(input()) # 마을의 수

마을 = list(map(int, input().split()))

print(sum(마을) - max(마을))