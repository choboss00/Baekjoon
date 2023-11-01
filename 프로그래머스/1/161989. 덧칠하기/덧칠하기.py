def solution(n, m, section):
    answer = 0
    check = 0
    while section:
        check = section[0] + m
        answer += 1
        while len(section) > 0 and section[0] < check:
            section.pop(0)
        
        
    return answer

# 페인트가 칠해진 길이가 n 미터인 벽
# 구역을 나누어 일부만 페인트 새로 칠하기 ( 1 ~ n번까지 번호를 붙임 )
# 롤러의 길이 : m 미터
# 규칙
# 롤러가 벽에서 벗어나면 안됨
# 구역의 일부분만 포함되도록 칠하면 안됨
# 다시 칠하기로 정한 구역은 적어도 한번 페인트칠을 해야 함