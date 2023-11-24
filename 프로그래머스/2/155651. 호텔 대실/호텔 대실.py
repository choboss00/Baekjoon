import heapq

def solution(book_time):
    answer = 0
    
    book_time.sort(key=lambda x : (x[0], x[1]))
    
    heap = []
    
    for time in book_time:
        # 시작시간, 마갑시간
        start, end = list(map(int, time[0].split(":"))), list(map(int, time[1].split(":")))
        # 분 단위로 처리
        start_sum = start[0] * 60 + start[1]
        end_sum = end[0] * 60 + end[1]
        
        # 힙에 아무런 값이 들어있지 않은 경우
        if len(heap) == 0:
            # 첫번째 원소 넣어주기
            heapq.heappush(heap, end_sum)
            answer += 1
        else:
            # 현재 가장 빨리 끝나는 시간 가져오기
            end_check = heapq.heappop(heap)
            # 시간 체크 ( 10분 추가 )
            if end_check + 10 <= start_sum:
                heapq.heappush(heap, end_sum)
            else:
                heapq.heappush(heap, end_check)
                heapq.heappush(heap, end_sum)
                answer += 1
    
    return answer

"""
1. 최소한의 객실만을 사용 -> 스케줄링, 힙을 쓰라는 뜻으로 이해했음
2. 한번 사용한 객실은 퇴실 시간을 기준으로 -> 퇴실 시간 기준으로 정렬해야 한다는 뜻으로 이해했음
3. 10분간 청소를 하고 다음 손님이 사용할 수 있음 -> 다음 손님을 받는데 10분이 걸림
4. 예약 시각이 문자열 형태로 담긴 2차원 배열

풀이
1. 힙 사용 ( 스케줄링 알고리즘 )
2. 퇴실 시간 기준으로 정렬
3. 10분 걸리는거 체크하기
"""