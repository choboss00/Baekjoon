/*
1. 5월 1일 기준
2. 주문 id, 제품 id, 출고일자, 출고여부를 조회하는 sql문 작성하기
3. 출고여부 : 5월 1일까지 출고완료, 이후 날짜는 출고대기, 미정이면 출고 미정
4. 주문 id 를 기준으로 오름차순 정렬
*/
select order_id, product_id, date_format(out_date, '%Y-%m-%d') out_date,
    case
        when out_date <= '2022-05-01' then '출고완료'
        when out_date > '2022-05-01' then '출고대기'
        else '출고미정'
    end as 출고여부
from food_order
order by 1