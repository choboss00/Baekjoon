def solution(picks, minerals):
    answer = 0
    # 곡괭이로 캘 수 있는 부분까지만 가져가기
    p_list = minerals[:sum(picks)*5]
    # 5개씩 자르기
    new_minerals = [[0,0,0] for _ in range(len(p_list)//5 + 1)]
    
    for i in range(len(p_list)):
        if minerals[i] == 'diamond':
            new_minerals[i//5][0] += 1
        elif minerals[i] == 'iron':
            new_minerals[i//5][1] += 1
        else:
            new_minerals[i//5][2] += 1
    
    # 정렬
    new_minerals.sort(key=lambda x : (-x[0], -x[1], -x[2]))
    
    # 순서대로 캐주기
    for dia, ir, st in new_minerals:
        for j in range(3):
            # 다이아 곡괭이
            if picks[j] > 0 and j == 0:
                picks[j] -= 1
                answer += (dia + ir + st)
                break
            elif picks[j] > 0 and j == 1:
                picks[j] -= 1
                answer += (dia * 5 + ir + st)
                break
            elif picks[j] > 0 and j == 2:
                picks[j] -= 1
                answer += (dia * 25 + ir * 5 + st)
                break
    return answer

"""
1. 마인 : 다이아, 철, 돌 ( 0 ~ 5개 )
- 곡괭이로 광물을 캘 때 피로도가 소모됨

2. 최소한의 피로도로 광물 캐기
- 사용할 수 있는 곡괭이 중 아무거나 하나를 선택해 광물을 캠
- 한 번 사용하기 시작한 곡괭이는 계속 사용 ( 5번 )
- 광물은 주어진 순서대로만 캘 수 있음
- 광산에 있는 모든 광물을 다 캐거나
- 더 사용할 곡괭이가 없을 때 까지 광물을 캠

3. picks : 곡괭이의 개수를 나타내는 정수 배열

4. minerals : 광물들의 순서를 나타내는 미네랄 배열

5. 마인이 작업을 끝내기까지 필요한 최소한의 피로도 return 하기

풀이
1. 곡괭이의 갯수와 미네랄의 갯수 체크하기
- 곡괭이로 다 캘수 있는경우, 없는 경우

"""