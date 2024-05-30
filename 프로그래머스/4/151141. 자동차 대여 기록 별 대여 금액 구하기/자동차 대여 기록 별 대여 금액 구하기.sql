-- 코드를 입력하세요
# 트럭 구하기
with truck_rental as (
    select crcc.car_id, crcrh.history_id, crcc.car_type, crcc.daily_fee, datediff(crcrh.end_date, crcrh.start_date)+1 as date
    from car_rental_company_car crcc
    join car_rental_company_rental_history crcrh using (car_id)
    where crcc.car_type = '트럭'
),
car_plan as (
    select plan_id, car_type, replace(duration_type, "일 이상", '') as duration, replace(discount_rate, '%', '') / 100 as rate
    from car_rental_company_discount_plan
)

select history_id, case when date < 7 then daily_fee * date
            when date < 30 then daily_fee * date * (1 - (select rate from car_plan where duration = 7 and car_type = '트럭'))
            when date < 90 then daily_fee * date * (1 - (select rate from car_plan where duration = 30 and car_type = '트럭'))
            else daily_fee * date * (1 - (select rate from car_plan where duration = 90 and car_type = '트럭'))
            end as fee
from truck_rental
order by 2 desc, 1 desc;