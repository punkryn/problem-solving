-- 코드를 작성해주세요
select count(id) FISH_COUNT, fish_name FISH_NAME
from fish_name_info name_info, fish_info info
where name_info.fish_type = info.fish_type
group by FISH_NAME
order by FISH_COUNT desc;