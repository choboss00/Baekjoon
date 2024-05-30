-- 코드를 작성해주세요
select year(ym) as year, round(avg(pm_val1), 2) as pm10, round(avg(pm_val2), 2) as 'pm2.5'
from air_pollution
where location2 = '수원'
group by 1
order by 1