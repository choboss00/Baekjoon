-- 코드를 입력하세요
SELECT book_id, date_format(published_date, '%Y-%m-%d') as published_date
from book
where published_date like '2021-%' and category = '인문'
order by published_date

-- 풀이
-- 1. 2021년에 출판됨
-- 2. '인문' 카테고리에 속하는 도서 리스트
-- 3. 도서 id, 출판일을 출력하는 sql문 작성하기
-- 4. 결과는 출판일을 기준으로 오름차순 정렬하기