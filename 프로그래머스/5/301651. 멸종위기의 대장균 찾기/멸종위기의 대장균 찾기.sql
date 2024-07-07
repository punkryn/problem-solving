with recursive tree as (
    select id, 1 as generation
    from ecoli_data d
    where parent_id is null
    union all
    select d.id, (generation + 1)
    from ecoli_data d, tree t
    where t.id = d.parent_id
), leaf as (
    select parent_id from ecoli_data d
    where parent_id is not null
    group by parent_id
)
select count(id) COUNT, generation GENERATION
from tree
where id not in (
    select parent_id from leaf
)
group by generation
order by generation asc;