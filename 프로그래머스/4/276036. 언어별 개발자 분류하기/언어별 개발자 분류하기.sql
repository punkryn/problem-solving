with front as (
    select sum(code) s from skillcodes where category = 'Front End' group by category
), python as (
    select code c from skillcodes where name = 'Python'
), C as (
    select code c from skillcodes where name = 'C#'
)
select
    (
        case 
            when skill_code & front.s and skill_code & python.c
                then 'A'
            when skill_code & C.c
                then 'B'
            when skill_code & front.s
                then 'C'
        end
    ) GRADE,
    ID,
    EMAIL
from DEVELOPERS, front, python, C
where (skill_code & front.s and skill_code & python.c)
or (skill_code & C.c)
or (skill_code & front.s)
order by GRADE, ID;