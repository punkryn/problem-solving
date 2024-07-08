-- 코드를 작성해주세요
select
    e.id,
    count(ee.id) child_count
from ecoli_data e
left join ecoli_data ee
on e.id = ee.parent_id
group by e.id
order by e.id asc;