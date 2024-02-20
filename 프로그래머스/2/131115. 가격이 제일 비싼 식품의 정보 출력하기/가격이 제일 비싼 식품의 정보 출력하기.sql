-- 코드를 입력하세요
-- 풀이
-- 1. 가격이 제일 비싼 식품의 식품 id, 식품 이름, 식품 코드, 식품분류, 식품 가격을 조회하는 sql 문 작성하기
select *
from food_product
order by price desc
limit 1