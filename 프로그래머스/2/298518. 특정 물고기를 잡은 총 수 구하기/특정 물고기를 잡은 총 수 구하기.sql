-- 코드를 작성해주세요
select
    count(*) FISH_COUNT
from fish_info fi, fish_name_info fni
where fi.fish_type = fni.fish_type
and fish_name in ('BASS', 'SNAPPER');
