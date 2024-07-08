-- 코드를 작성해주세요
select 
    year(e.differentiation_date) YEAR,
    (max_size.ms - e.size_of_colony) YEAR_DEV,
    id
from ECOLI_DATA e
join (
    select max(size_of_colony) ms, year(differentiation_date) year2
    from ecoli_data e group by year2
) max_size
on year(e.differentiation_date) = max_size.year2
order by year(e.differentiation_date) asc, YEAR_DEV asc;