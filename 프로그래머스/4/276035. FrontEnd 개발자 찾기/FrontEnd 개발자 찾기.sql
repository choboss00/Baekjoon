-- 풀이
-- skillcodes : 개발자들이 사용하는 프로그래밍 언어에 대한 정보를 담은 테이블
-- developers : 개발자들의 프로그래밍 스킬 정보를 담은 테이블
-- developers 테이블에서 front end 스킬을 가진 개발자의 정보를 조회하려고 함
-- 조건에 맞는 개발자의 id, 이메일, 이름, 성을 조회하는 sql 문 작성하기
-- 결과는 id 를 기준으로 오름차순 정렬
select distinct(d.id), d.email, d.first_name, d.last_name
from skillcodes s, developers d
where d.skill_code & s.code > 0 and s.category = 'Front End'
order by 1