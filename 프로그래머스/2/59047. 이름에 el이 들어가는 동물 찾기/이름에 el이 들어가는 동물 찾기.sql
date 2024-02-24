/*
1. 할머니가 기르던 개는 이름에 el 이 들어감

2. 동물 보호소에 들어온 동물 이름 중, 이름에 el 이 들어가는 개의 아이디와 이름을 조회하는 sql문 작성하기

3. 결과는 이름 순으로 조회
*/
select animal_id, name
from animal_ins
where name like '%el%' and animal_type = 'dog'
order by 2