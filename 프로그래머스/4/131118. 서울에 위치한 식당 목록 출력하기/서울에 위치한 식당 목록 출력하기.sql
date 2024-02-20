-- 코드를 입력하세요
select i.rest_id, i.rest_name, i.food_type, i.favorites, i.address, round(avg(r.review_score), 2) as score
from rest_info i join rest_review r on (i.rest_id = r.rest_id)
group by i.rest_id
having address like "서울%"
order by score desc, favorites desc



-- 풀이
-- 1. 식당의 정보를 담은 rest_info table
-- 2. 식당의 리뷰 정보를 담은 rest_review table
-- 3. rest_id 와 연관관계
-- 4. rest_info, rest_review 테이블에서 서울에 위치한 식당들의 식당 id, 식당 이름, 음식 종류, 즐겨찾기 수, 주소, 리뷰 평균 점수를 조회하는 sql 문 작성하기
-- 5. 리뷰 평균점수는 소수점 세번째 자리에서 반올림하기
-- 6. 결과는 평균점수를 기준으로 내림차순 정렬, 평균점수가 같다면 즐겨찾기 수를 기준으로 내림차순 정렬하기