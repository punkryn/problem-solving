-- 코드를 작성해주세요
select 
    g.EMP_NO,
    EMP_NAME, (
        case
            when avg(g.score) >= 96
                then 'S'
            when avg(g.score) >= 90
                then 'A'
            when avg(g.score) >= 80
                then 'B'
            else 'C'
        end
    ) GRADE, (
        case
            when avg(g.score) >= 96
                then 0.2
            when avg(g.score) >= 90
                then 0.15
            when avg(g.score) >= 80
                then 0.1
            else 0
        end
    ) * e.SAL BONUS
from HR_GRADE g, HR_EMPLOYEES e, HR_DEPARTMENT d
where g.emp_no = e.emp_no and e.dept_id = d.dept_id
group by EMP_NO;