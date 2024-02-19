-- 코드를 입력하세요
SELECT animal_id, name, datetime
from animal_ins
order by name, datetime desc

-- 모든 동물의 아이디, 이름, 보호 시작일을 이름 순으로 조회하는 sql문 작성하기
-- 풀이
-- 1. name 순으로 정렬하기
-- 2. 이름이 같은 동물 중에서는 보호를 나중에 시작한 동물을 먼저 보여줘야 함