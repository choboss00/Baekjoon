-- 코드를 입력하세요
SELECT member_id, member_name, gender, date_format(date_of_birth, '%Y-%m-%d') date_of_birth
from member_profile
where date_of_birth like '%-03-%' and tlno is not null and gender = 'W'
order by member_id

-- 풀이
-- 1. 생일이 3월
-- 2. 여성 회원
-- 3. id, 이름, 성별, 생년월일 조회하는 sql문 작성하기
-- 4. 전화번호가 null 인 경우는 출력 대상에서 제외
-- 5. 회원 id 를 기준으로 오름차순 정렬하기