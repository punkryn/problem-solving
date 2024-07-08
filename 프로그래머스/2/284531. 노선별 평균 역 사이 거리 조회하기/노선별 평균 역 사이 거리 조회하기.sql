-- 코드를 작성해주세요
select
    route,
    concat(round(sum(d_between_dist), 1), 'km') TOTAL_DISTANCE,
    concat(round(avg(d_between_dist), 2), 'km') AVERAGE_DISTANCE
from subway_distance s
group by 1
order by sum(d_between_dist) desc;