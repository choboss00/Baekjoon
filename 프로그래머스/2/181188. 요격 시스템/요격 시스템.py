import heapq

def solution(targets):
    answer = 0
    
    targets.sort(key = lambda x : (x[1], x[0]))
    
    heap = []
    
    for target in targets:
        # 힙의 길이가 0 일 경우
        if len(heap) == 0:
            heapq.heappush(heap, -target[1])
            answer += 1
        else:
            # 힙 안에 들어있는 원소와 비교하기
            heap_num = abs(heapq.heappop(heap))
            
            # 그 다음 원소의 첫번째 값과 비교
            # 만약 현재 힙의 원소가 더 클 경우 다시 넣어주기
            if heap_num > target[0]:
                heapq.heappush(heap, -heap_num)
            else:
                heapq.heappush(heap, -target[1])
                answer += 1
    return answer

