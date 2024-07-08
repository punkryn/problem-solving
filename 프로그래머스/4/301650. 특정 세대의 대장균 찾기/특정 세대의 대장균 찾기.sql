-- 코드를 작성해주세요
select C.id
from (
    select id from ecoli_data where parent_id is null
) A
join ecoli_data B
on A.id = B.parent_id
join ecoli_data C
on B.id = C.parent_id
order by C.id;