-- 코드를 작성해주세요
select concat(quarter(differentiation_date), 'Q') as quarter, count(*) as ecoli_count
from ecoli_data
group by 1
order by 1;