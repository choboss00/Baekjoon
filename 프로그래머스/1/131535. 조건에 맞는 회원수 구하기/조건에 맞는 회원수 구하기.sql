-- 코드를 입력하세요
select count(*) as users
from user_info
where joined like '2021%' and age between 20 and 29


-- 풀이
-- 1. 2021 년에 가입한 회원
-- 2. 나이가 20세 이상 29세 이하