-- 코드를 작성해주세요
select
    year(ym) YEAR,
    round(avg(pm_val1), 2) as PM10,
    round(avg(pm_val2), 2) as 'PM2.5'
from air_pollution a
where location2 = '수원'
group by YEAR
order by YEAR;