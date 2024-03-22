import math
from itertools import permutations

def solution(numbers):
    ans = 0
    ans_set = set()
    for i in range(1, len(numbers) + 1):
        permute = list(permutations(numbers, i))
        permute = set(list(map(lambda x: int(''.join(x)), permute)))
        ans_set = ans_set.union(permute)
    ans_set = list(filter(lambda x : x > 1, list(ans_set)))
    
    for a in ans_set:
        check = False
        for i in range(2, int(math.sqrt(a)) + 1):
            if a % i == 0:
                check = True
                break
        if not check:
            ans += 1
    
    return ans
"""
## 소수 찾기
1. 한자리 숫자가 적힌 종이 조각

2. 흩어진 종이 족가을 붙여 소수를 몇 개 만들 수 있는지 판단하기

3. 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers

4. 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하는 solution 함수 작성하기

## 풀이
1. 순열 + 소수판별하기
"""