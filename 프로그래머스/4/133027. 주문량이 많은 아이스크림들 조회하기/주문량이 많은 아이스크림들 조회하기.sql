-- 풀이
-- 1. first_half : 아이스크림 가게의 상반기 주문 정보를 담은 테이블
-- 2. july : 7월의 아이스크림 주문 정보를 담은 테이블
-- 3. shipment_id : 외래키 ( 조인 )
-- 4. 7월 아이스크림 총 주문량과
-- 5. 상반기의 아이스크림 총 주문량을 더한 값이
-- 6. 큰 순서대로 상위 3개의 맛을 조회하는 sql 문 작성하기
with temp as (
    select shipment_id, flavor, sum(total_order) total_order
    from july
    group by flavor
)

select t.flavor
from temp t
join first_half fh on (t.shipment_id = fh.shipment_id)
group by 1
order by sum(t.total_order + fh.total_order) desc
limit 3