-- 코드를 작성해주세요
select 
    count(*) FISH_COUNT,
    max(length) MAX_LENGTH,
    FISH_TYPE
from fish_info fi
group by fish_type
having avg(COALESCE(length, 10)) >= 33
order by fish_type asc;