-- 코드를 입력하세요
SELECT flavor
from first_half
order by total_order desc, shipment_id

-- 풀이
-- 1. 상반기에 판매된 아이스크림의 맛
-- 2. 총주문량을 기준으로 내림차순 정렬
-- 3. 총주문량이 같다면 추랗 번호를 기준으로 오름차순 정렬