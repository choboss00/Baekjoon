-- 코드를 입력하세요
SELECT car_id, round(avg(datediff(end_date, start_date)+1), 1) as average_duration
from car_rental_company_rental_history
group by 1
having round(avg(datediff(end_date, start_date)+1), 1) >= 7
order by 2 desc, 1 desc;