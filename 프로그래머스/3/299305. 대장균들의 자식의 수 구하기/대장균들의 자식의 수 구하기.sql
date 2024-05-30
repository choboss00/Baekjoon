-- 코드를 작성해주세요
with child_data as (
    select parent_id as id, count(*) as child_count
    from ecoli_data
    group by 1
)

select A.id, ifnull(child_count, 0) as child_count
from ecoli_data A
left outer join child_data B on (A.id = B.id)