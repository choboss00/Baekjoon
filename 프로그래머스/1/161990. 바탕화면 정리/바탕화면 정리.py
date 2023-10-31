def solution(wallpaper):
    answer = [55, 55, 0, 0]
    file_list = []
    # 파일들이 위치한 점 구하기
    for y in range(len(wallpaper)):
        for x in range(len(wallpaper[y])):
            if wallpaper[y][x] == '#':
                file_list.append((x,y))
    print(file_list)
    # 파일들의 점 중, 가장 왼쪽에 붙고 가장 위에 붙은 점 S 구하기
    # 파일들의 점 중, 가장 오른쪽에 붙고 가장 아래에 붙은 점 E 구하기
    for file in file_list:
        # 가장 왼쪽 lux
        if file[1] < answer[0]:
            answer[0] = file[1]
        # 가장 위 luy
        if file[0] < answer[1]:
            answer[1] = file[0]
        # 가장 오른쪽 rdx
        if answer[2] < file[1]:
            answer[2] = file[1]
        # 가장 아래 rdy
        if answer[3] < file[0]:
            answer[3] = file[0]
    answer[2] += 1
    answer[3] += 1
    return answer

# 저장해둔 파일 삭제
# 바탕화면 : 사각형인 격자판 ( wallpaper )
# 빈칸 : . , 파일이 있는 칸 : #
# 드래그를 하면 파일들을 선택할 수 있고, 선택된 파일들을 삭제할 수 있음
# 최소한의 이동거리를 갖는 한번의 드래그로 모든 파일 지우기
# 격자점 S -> E 로 드래그
# 드래그한 거리 : | rdx - lux | + | rdy - luy | (점 E 에서 점 S 를 뺀 절댓값 )
# S 의 점 구하기 : 가장 왼쪽에 붙은 점, 가장 위쪽의 점
# E 의 점 구하기 : 가장 오른쪽에 붙은 점, 가장 아래에 붙은 점
