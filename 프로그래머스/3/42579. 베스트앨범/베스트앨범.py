def solution(genres, plays):
    answer = []
    
    genre_play_dict = {}
    
    for i in range(len(genres)):
        if genres[i] not in genre_play_dict:
            genre_play_dict[genres[i]] = plays[i]
            continue
        genre_play_dict[genres[i]] += plays[i]
    # 우선순위 정렬
    genre_play_dict = sorted(genre_play_dict.items(), key=lambda x: -x[1])
    
    genre_index_dict = {}
    
    for i in range(len(genres)):
        if i not in genre_index_dict:
            genre_index_dict[i] = [genres[i], plays[i]]
    
    genre_index_dict = sorted(genre_index_dict.items(), key=lambda x: -x[1][1])
    
    for genre, play in genre_play_dict:
        genre_cnt = 0 # 최대 2개
        for key, value in genre_index_dict:
            if genre == value[0]:
                genre_cnt += 1
                answer.append(key)
                
                if genre_cnt == 2:
                    break
                
    
    return answer

"""
## 베스트앨범

## 문제
1. 장르 별로 가장 많이 재생된 노래를 두개씩 모아 베스트 앨범을 출시하려고 함

2. 노래 : 고유 번호로 구분

3. 노래를 수록하는 기준
- 속한 노래가 많이 재생된 장르를 먼저 수록함
- 장르 내에서 많이 재생된 노래를 먼저 수록함
- 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록함

4. 노래의 장르를 나타내는 문자열 배열 genres

5. 노래별 재생 횟수를 나타내는 정수 배열 plays

6. 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하는 함수 작성하기

## 풀이
1. 입출력 예시
- classic 장르 : 1450회 재생
- pop 장르 : 3100회 재생

그러므로 pop 장르의 노래를 먼저, 그 다음 classic 장르의 노래를 2개씩 묶어서 수록함

2. 딕셔너리 활용 : 고유 번호를 사용하므로, key-value 꼴인 딕셔너리 활용

"""