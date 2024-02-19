-- 코드를 입력하세요
select f.flavor
from first_half f join icecream_info i on (f.flavor = i.flavor)
where f.total_order > 3000 and i.ingredient_type like 'fruit_%'
order by f.total_order desc

-- 풀이
-- 1. 2개의 테이블
-- - 아이스크림 가게의 상반기 주문 정보를 담은 first_half
-- - 아이스크림 성분에 대한 정보를 담은 icecream_info
-- 2. icecream_info 의 기본 키는 flavor
-- 3. first_half 테이블의 외래 키는 flavor
-- 4. 상반기 아이스크림 총주문량이 3000 보다 높음
-- 5. 아이스크림의 주 성분이 과일
-- 6. 총주문량이 큰 순서대로 조회하는 sql 문 작성하기