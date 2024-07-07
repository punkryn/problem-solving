-- 코드를 작성해주세요
select
    SUM(SCORE) SCORE,
    g.EMP_NO,
    EMP_NAME,
    POSITION,
    EMAIL
FROM HR_GRADE g
JOIN HR_EMPLOYEES e ON g.emp_no = e.emp_no
JOIN HR_DEPARTMENT d ON e.dept_id = d.dept_id
WHERE g.EMP_NO = (
    select EMP_NO from (
        select EMP_NO, sum(score) s from HR_GRADE group by EMP_NO
    ) A
    order by A.s desc
    LIMIT 1
)
GROUP BY EMP_NO;