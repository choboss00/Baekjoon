-- 코드를 입력하세요
SELECT DATE_FORMAT(X.SALES_DATE, '%Y-%m-%d') as SALES_DATE, X.PRODUCT_ID, X.USER_ID, X.SALES_AMOUNT
FROM (
    SELECT SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
    FROM ONLINE_SALE
    UNION ALL
    SELECT SALES_DATE, PRODUCT_ID, NULL, SALES_AMOUNT
    FROM OFFLINE_SALE
) X
WHERE X.SALES_DATE LIKE '%2022-03%'
ORDER BY X.SALES_DATE, X.PRODUCT_ID, X.USER_ID


-- ONLINE_SALE, OFFLINE_SALE 테이블
-- 테이블에서 2022년 3월의 오프라인/온라인 상품 판매 데이터의 판매 날짜 상품ID, 유저ID, 판매량을 출력하는 SQL 문 작성하기
-- OFFLINE_SALE 테이블의 판매 데이터의 USER_ID 값은 NULL 로 표시하기
-- 판매일을 기준으로 오름차순 정렬, 판매일이 같다면 상품 ID 를 기준으로 오름차순, 상품ID 까지 같다면 유저 ID 를 기준으로 오름차순 정렬하기
-- 풀이
-- 1. 2022년 3월 데이터 가져오기
-- 2. OFFLINE_SALE 테이블 USER_ID 값 NULL 처리하기
-- 3. UNION ALL 하기
-- 4. 정렬하기