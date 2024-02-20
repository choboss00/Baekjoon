-- 코드를 입력하세요
-- 풀이
-- 1. 가장 최근에 들어온 동물은 언제 들어왔는지 조회하는 sql 문 작성하기
select max(datetime) as 시간
from animal_ins
