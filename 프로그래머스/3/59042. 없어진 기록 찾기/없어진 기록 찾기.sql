-- 풀이
-- 1. animal_ins : 동물 보호소에 들어온 동물의 정보를 담은 테이블
-- 2. animal_outs : 동물 보호소에서 입양 보낸 동물의 정보를 담은 테이블
-- 3. animal_id : 외래 키
-- 4. 입양을 간 기록은 있는데, 보호소에 들어온 기록이 없는 동물의 id 와
-- 5. 이름을 id 순으로 조회하는 sql 문 작성하기
-- 6. left outer join
select ao.animal_id, ao.name
from animal_outs ao
left join animal_ins ai on (ao.animal_id = ai.animal_id)
where ai.animal_id is null
order by 1
