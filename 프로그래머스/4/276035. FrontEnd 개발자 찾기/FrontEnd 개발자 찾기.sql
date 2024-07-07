with front as (
    select code from skillcodes where category = 'Front End'
)
select id, email, first_name, last_name
from developers
where (
    select count(*) 
    from (
        select 1 from front where code & skill_code
    ) A
) >= 1
order by id asc;