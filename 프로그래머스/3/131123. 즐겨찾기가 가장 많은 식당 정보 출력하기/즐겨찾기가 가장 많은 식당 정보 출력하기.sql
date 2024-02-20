-- 코드를 입력하세요
-- 풀이
-- 1. 테이블에서 음식종류별로
-- 2. 즐겨찾기 수가 가장 많은 식당의 음식 종류, id, 식당 이름, 즐겨찾기 수를 조회하는 sql문 작성하기
-- 3. 결과는 음식 종류를 기준으로 내림차순 정렬하기
select food_type, rest_id, rest_name, favorites
from rest_info r
where r.favorites = (
    select max(favorites)
    from rest_info i
    where r.food_type = i.food_type
)
order by food_type desc