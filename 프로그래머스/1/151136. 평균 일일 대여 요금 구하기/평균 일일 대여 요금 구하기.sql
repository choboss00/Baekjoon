-- 코드를 입력하세요
SELECT round(avg(daily_fee), 0) as average_fee
from car_rental_company_car
where car_type = 'SUV'
group by car_type

-- 풀이
-- 1. 자동차 종류 : 'SUV'
-- 2. 평균 일일 대여 요금 소숫점 첫번째 자리에서 반올림, 컬럼명 average_fee