-- 코드를 입력하세요
SELECT factory_id, factory_name, address
from food_factory
where address like '강원도%'
order by factory_id

-- 풀이
-- 1. 식품공장의 공장 id, 공장 이름, 주소를 조회하는 sql문 작성하기
-- 2. 공장 id 를 기준으로 오름차순 정렬
-- 3. 강원도에 위치