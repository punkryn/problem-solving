-- 코드를 작성해주세요
select 
    id,
    fish_name,
    length
from fish_info fi, fish_name_info fni
where fi.fish_type = fni.fish_type
and (fi.fish_type, length) in (
    select
        fish_type,
        max(length) ml
    from fish_info fi
    group by fish_type
)
order by id asc;