/*
풀이
1. 상품 카테고리 코드 별 상품 개수 출력하는 sql문 작성하기
2. 상품 카테고리 코드를 기준으로 오름차순 정렬
*/
select left(product_code, 2) category, count(*) products
from product
group by 1
order by 1