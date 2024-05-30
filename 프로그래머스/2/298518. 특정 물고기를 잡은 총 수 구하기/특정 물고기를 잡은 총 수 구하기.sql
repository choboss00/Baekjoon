-- 코드를 작성해주세요
select count(*) as fish_count
from fish_info
join fish_name_info using (fish_type)
where fish_name = 'BASS' or fish_name = 'SNAPPER';