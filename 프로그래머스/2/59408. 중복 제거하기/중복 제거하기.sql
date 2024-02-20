-- 코드를 입력하세요
-- 풀이
-- 1. 동물 보호소에 들어온 동물의 이름은 몇 개인지 조회하는 sql 문 작성하기
-- 2. 이름이 null 인 경우는 집계 X, 중복되는 이름은 하나로 침
with temp as ( 
    select *
    from animal_ins
    where name is not null
    group by name )
select count(*) as count
from temp