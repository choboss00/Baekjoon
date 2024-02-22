-- 풀이
-- 1. car_rental_company_car : 회사에서 대여중인 자동차들의 정보를 담은 테이블
-- 2. car_rental_company_rental_history : 자용차 대여 기록 정보를 담은 테이블
-- 3. car_rental_company_discount_plan : 자동차 종류 별 대여 기간 종류 병 할인 정책 정보를 담은 테이블
-- 4. 자동차 종류 : 세단 또는 SUV
-- 5 : 2022년 11월 1일 ~ 2022년 11월 30일까지 대여 가능하고
-- 6. 30일간의 대여 금액이 50만원 이상 200만원 미만인 자동차에 대해서
-- 7. 자동차 ID, 자동차 종류, 대여 금액 리스트를 출력하는 SQL 문 작성하기
-- 8. 대여 금액을 기준으로 내림차순 정렬
-- 9. 대여 금액이 같은 경우 자동차 종류를 기준으로 오름차순 정렬
-- 10. 자동차 종류까지 같은 경우 자동차 ID 를 기준으로 내림차순 정렬하기
-- 로직
-- 1. 자동차 종류에 맞는 임시 테이블 생성
-- 2. 대여 가능 날짜에 맞춘 임시 테이블 생성
-- 3. PLAN 테이블과 CAR 테이블을 CAR_TYPE JOIN 해서 할인 가격 계산하기 ( FEE )
-- 4. 30일간의 대여금액이 50만원 이상, 200만원 미만인 자동차 조건 걸기
-- 5. HISTORY 테이블과 조인 후 SELECT
with temp as (
    select car_id, max(end_date) as end_date
    from car_rental_company_rental_history
    group by car_id
    having year(max(end_date)) <= 2022 and month(max(end_date)) <= 10
), temp2 as (
    select t.car_id, c.car_type, c.daily_fee
    from temp t
    join car_rental_company_car c on (t.car_id = c.car_id)
    where c.car_type in ('SUV', '세단')
), temp3 as (
    select t2.car_id, t2.car_type, round(t2.daily_fee * 30 * (100 - p.discount_rate) / 100, 0) fee
    from temp2 t2
    join car_rental_company_discount_plan p on (t2.car_type = p.car_type)
    where p.duration_type = '30일 이상'
)

select car_id, car_type, fee
from temp3
where fee between 500000 and 1999999
order by 3 desc, 2 asc, 1 desc