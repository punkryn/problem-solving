-- 코드를 입력하세요
SELECT
    a.author_id,
    a.author_name,
    b.category,
    sum(sales * price) total_sales
from (
    select *
    from book_sales
    where left(sales_date, 7) = '2022-01'
) bs
join book b on bs.book_id = b.book_id
join author a on b.author_id = a.author_id
group by a.author_id, b.category
order by a.author_id asc, b.category desc;