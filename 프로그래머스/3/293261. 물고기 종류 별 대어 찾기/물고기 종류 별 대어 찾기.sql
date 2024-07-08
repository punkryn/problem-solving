-- 코드를 작성해주세요
select 
    id,
    fish_name,
    length
from fish_info fi, fish_name_info fni
where fi.fish_type = fni.fish_type
and (fish_name, length) in (
    select
        fish_name,
        max(length) ml
    from fish_info fi, fish_name_info fni
    where fi.fish_type = fni.fish_type
    group by fish_name
)
order by id asc;
