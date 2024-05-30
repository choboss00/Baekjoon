-- 코드를 입력하세요
SELECT ao.animal_id, ao.name
from animal_outs ao
join animal_ins ai using (animal_id)
order by datediff(ao.datetime, ai.datetime) desc
limit 2