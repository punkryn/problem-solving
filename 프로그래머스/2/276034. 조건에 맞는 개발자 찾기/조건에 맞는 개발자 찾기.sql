select id, email, first_name, last_name
from developers
where (skill_code & (select code from skillcodes where name = 'python'))
+ (skill_code & (select code from skillcodes where name = 'C#'))
order by id asc;