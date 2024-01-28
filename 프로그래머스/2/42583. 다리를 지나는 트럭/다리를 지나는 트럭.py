from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 1
    
    # 2개의 큐 활용
    truck_weights = deque(truck_weights)
    truck_bridge = deque()
    
    bridge_weight = 0
    
    # 첫번째 트럭 넣기
    truck_bridge.append([truck_weights.popleft(), 1])
    
    bridge_weight += truck_bridge[0][0]
    
    while bridge_weight > 0 or truck_weights:
        if len(truck_weights) > 0:
            truck = truck_weights.popleft()

            bridge_weight += truck # 트럭의 무게만큼 더하기

            if bridge_weight > weight:
                bridge_weight -= truck
                truck_weights.appendleft(truck)
            else:
                truck_bridge.append([truck, 0]) # 도로 위에 추가하기

        # 시간 증가
        for i in range(len(truck_bridge)):
            truck_bridge[i][1] += 1
        
        answer += 1
        
        # 다리를 지날 수 있는 경우
        while truck_bridge:
            tr, t = truck_bridge.popleft()
            
            if t == bridge_length:
                bridge_weight -= tr
                continue
            
            truck_bridge.appendleft([tr, t])
            break
    return answer + 1

"""
## 다리를 지나는 트럭

## 문제
1. 트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순으로 건너려 함

2. 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 구하기

3. 다리에는 트럭이 최대 bridge_length 대 만큼 올라갈 수 있음

4. 다리는 weight 이하까지의 무게를 견딜 수 있음
- 다리에 완전히 오르지 않은 트럭의 무게는 무시함

5. 예시
- bridge_length = 2, weight = 10
- 무게 리스트 : [7, 4, 5, 6] 인 트럭이 순서대로 최단 시간 안에 다리를 건너는 방법
- 0초 : 트럭 대기
- 1초 : 7kg 트럭 다리 건너는 중, 4kg 트럭 대기 ( 10 키로 초과 )
- 2초 : 7kg 트럭 다리 건너는 중
- 3초 : 7kg 트럭 다리 다 건넘, 4kg 트럭 다리 건너는 중
- 4초 : 4kg 트럭 다리 건너는 중, 5kg 트럭 다리 건너는 중
- 5초 : 4kg 트럭 다리 다 건넘, 5kg 트럭 다리 건너는 중, 6kg 트럭 대기 ( 10 키로 초과 )
- 6초 : 5kg 트럭 다리 다 건넘, 6kg 트럭 다리 건너는 중
- 7초 : 6kg 트럭 다리 건너는 중
- 8초 : 트럭 다 건너옴

## 입력
1. bridge_length : 다리 길이, 다리 길이 만큼 초가 지나야 다리를 다 건넘
2. weight : 다리가 버틸 수 있는 무게
3. truck_weights : 트럭 수와 각 트럭 별 kg

## 출력
1. 모든 트럭이 다 지나간 뒤 시간 return

## 풀이
1. deque 활용 ( 트럭의 가장 첫번째부터 출발해야 함 )

2. 2개의 queue 활용
- truck_weigths : 대기중인 트럭
- truck_bridge : 다리 위에서 지나가고 있는 트럭
- 다리 위에서 지나가고 있는 트럭의 무게들과 가장 앞에서 대기중인 트럭의무게를 합친 값과 weights 비교
- 비교 후, 탈 수 있으면 올라가고 그렇지 않으면 대기
- 다리 위에서 bridge_length 만큼 시간이 지났을 경우, pop

3. 최종 시간 return

"""