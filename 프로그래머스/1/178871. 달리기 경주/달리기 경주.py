def solution(players, callings):
    player_dict = {player : i for i, player in enumerate(players)}
    
    for calling in callings:
        # 플레이어 등수 가져오기
        idx = player_dict[calling]
        # 등수 교체
        player_dict[calling] -= 1
        player_dict[players[idx-1]] += 1
        # 자리바꾸기
        players[idx], players[idx-1] = players[idx-1], players[idx]
    
    return players

# 자기 바로 앞의 선수를 추월할 때 추월한 선수의 이름을 부름
# soe -> soe 선수가 1등인 mumu 선수를 추월 ( 등수 바뀜 )
# players : 차례대로 등수가 담긴 배열
# 해설진이 부른 이름을 담은 문자열 배열 : callings
# 경주가 끝났을 때 선수들의 이름을 1등부터 등수 순서대로 배열에 담아 리턴하기

# 자리바꾸는 문제 -> stack 으로 풀어볼까?
# callings 의 배열을 가지고 player 배열의 자리를 바꾸기
# 같은 이름이 나올 때 까지 pop 한 이름을 저장하는 배열