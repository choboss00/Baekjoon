-- 코드를 작성해주세요
with max_fish_info as (
    select fish_type, max(length) as length
    from fish_info
    group by 1
)

select A.id, B.fish_name, A.length
from fish_info A
join fish_name_info B using (fish_type)
where (A.fish_type, A.length) in (
    select *
    from max_fish_info
)