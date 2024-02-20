-- 코드를 입력하세요
-- 풀이
-- 1. product table 에서 판매 중인 상품 중 가장 높은 판매가를 출력하는 sql 문 작성하기
-- 2. 컬럼 명은 max_price 로 바꾸기
select price as max_price
from product
where price = (
    select max(price)
    from product
)