-- 풀이
-- 1. skillcodes : 개발자들이 사용하는 프로그래밍 언어에 대한 정보를 담은 테이블
-- 2. developers : 개발자들의 프로그래밍 스킬 정보를 담은 테이블
-- 3. 어떤 개발자의 skill_code 가 400 이라면, 이는 skillcodes 테이블에서 code 가 256, 128, 16 에 해당하는 스킬을 가졌다는 걸 의미함
-- 4. developers 테이블에서 python 이나 c# 을 가진 개발자의 정보 조회
-- 5. 조건에 맞는 개발자의 id, 이메일, 이름 성을 조회하는 sql문 작성하기
-- 6. 결과는 id 를 기준으로 오름차순 정렬하기
-- 7. skill_code 와 code 비트연산
select distinct(d.id), d.email, d.first_name, d.last_name
from developers d, skillcodes s
where d.skill_code & s.code > 0 and s.name in ('C#', 'Python')
order by 1