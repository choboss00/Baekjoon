n, m = map(int, input().split())
childs = list(map(int, input().split()))

# 키차이 리스트
child_list = []

for i in range(1, n):
    child_list.append(childs[i]-childs[i-1])

# 키차이 리스트 정렬
child_list.sort()

ans = 0

"""
만약 m = 1 일 경우, 키차이 리스트를 다 더한값이 정답
만약 m = 2 일 경우, 키차이 리스트에서 가장 큰 값을 뺀 값이 정답
...
"""
for j in range(n-m):
    ans += child_list[j]

print(ans)
