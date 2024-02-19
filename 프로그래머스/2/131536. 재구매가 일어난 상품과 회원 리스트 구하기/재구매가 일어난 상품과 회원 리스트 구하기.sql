-- 코드를 입력하세요
SELECT USER_ID, PRODUCT_ID
FROM ONLINE_SALE
GROUP BY USER_ID, PRODUCT_ID
HAVING COUNT(PRODUCT_ID) > 1
ORDER BY USER_ID, PRODUCT_ID DESC

-- 동일한 회원이 동일한 상품을 재구매한 데이터를 구하기
-- 재구매한 회원 ID 와 재구매한 상품 ID 를 출력하는 SQL 문 작성하기
-- 회원 ID 기준 오름차순 정렬, 회원 ID 가 같다면 상품 ID 를 기준으로 내림차순 정렬하기