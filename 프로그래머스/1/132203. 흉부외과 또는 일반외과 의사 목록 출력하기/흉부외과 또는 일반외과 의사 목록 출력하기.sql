-- 코드를 입력하세요
SELECT dr_name, dr_id, mcdp_cd, date_format(hire_ymd, '%Y-%m-%d') as hire_ymd
from doctor
where mcdp_cd in ('CS', 'GS')
order by hire_ymd desc, dr_name

-- 풀이
-- 1. 진료과가 흉부외과 이거나 일반외과
-- 2. 이름, 의사id, 진료과, 고용일자를 조회하는 sql문
-- 3. 결과는 고용일자를 기준으로 내림차순 정렬
-- 4. 고용일자가 같다면 이름을 기준으로 오름차순 정렬