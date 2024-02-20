-- 코드를 작성해주세요
-- 풀이
-- 1. 희귀도가 LEGEND 인 아이템들의 가격 총합 구하기
-- 2. 컬럼명은 TOTAL_PRICE 로 지정하기
select sum(price) as total_price
from item_info
where rarity = 'LEGEND'
group by rarity