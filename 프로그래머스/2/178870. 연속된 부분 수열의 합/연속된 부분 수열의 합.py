def solution(sequence, k):
    left, right = 0, 1
    ans = []
    
    # 누적합
    sequence_list = [0]
    
    for i in range(1, len(sequence)+1):
        seq = sequence_list[i-1] + sequence[i-1]
        sequence_list.append(seq)
    
    while left <= right and right <= len(sequence):
        s = sequence_list[right] - sequence_list[left]
        
        if s < k:
            right += 1
        elif s == k:
            ans.append([left, right-1])
            left += 1
            right += 1
        else:
            left += 1
    
    ans.sort(key=lambda x : ((x[1]-x[0]), x[0]))    
    
    return ans[0]

"""
1. 비내림차순으로 정렬된 수열이 주어질 때, 조건을 만족하는 부분 수열 찾기
- 기존 수열에서 임의의 두 인덱스의 원소와 그 사이의 원소를 모두 포함하는 부분수열
- 부분 수열의 합 : k
- 합이 k 인 부분 수열이 여러개 -> 짧은 수열 찾기
- 길이가 짧은 수열이 여러개 -> 시작 인덱스가 작은 수열 찾기

2. 
"""