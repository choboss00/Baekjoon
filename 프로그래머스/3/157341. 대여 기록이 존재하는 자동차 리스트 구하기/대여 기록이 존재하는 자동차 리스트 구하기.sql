-- 코드를 입력하세요
SELECT distinct (car_id)
from car_rental_company_rental_history crcrh
join car_rental_company_car crcc using(car_id)
where crcc.car_type = '세단' and month(crcrh.start_date) = 10
order by 1 desc