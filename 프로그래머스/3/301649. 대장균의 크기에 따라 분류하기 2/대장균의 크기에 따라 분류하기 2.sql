with A as (
    select id, percent_rank() over(order by size_of_colony desc) pr
    from ecoli_data
)
select 
    id, (
        case
            when A.pr <= 0.25 then 'CRITICAL'
            when A.pr <= 0.50 then 'HIGH'
            when A.pr <= 0.75 then 'MEDIUM'
            else 'LOW'
        end
    ) colony_name
from A
order by id;