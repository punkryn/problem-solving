-- 코드를 입력하세요
select flavor
from (SELECT flavor, sum(total_order) total
from (
    select * from first_half
    union all
    select * from july
) B
group by flavor
order by total desc
limit 3) A;