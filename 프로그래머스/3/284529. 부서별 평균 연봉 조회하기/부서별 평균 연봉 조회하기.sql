-- 코드를 작성해주세요
select
    d.dept_id,
    dept_name_en,
    round(avg(e.sal), 0) AVG_SAL
from HR_EMPLOYEES e, HR_DEPARTMENT d
where e.dept_id = d.dept_id
group by d.dept_id
order by AVG_SAL desc;