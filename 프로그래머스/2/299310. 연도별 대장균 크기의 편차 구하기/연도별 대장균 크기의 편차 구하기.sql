-- 코드를 작성해주세요
with date_ecoli_data as (
    select year(differentiation_date) as year, max(size_of_colony) as max_size
    from ecoli_data
    group by 1
)

select year(differentiation_date) as year,
       (select max_size - ecoli_data.size_of_colony
        from date_ecoli_data
        where date_ecoli_data.year = year(ecoli_data.differentiation_date)) as year_dev, id
from ecoli_data
order by 1, 2;