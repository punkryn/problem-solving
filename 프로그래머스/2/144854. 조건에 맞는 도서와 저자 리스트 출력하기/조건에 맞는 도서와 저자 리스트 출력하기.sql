-- 코드를 입력하세요
SELECT book_id, author_name, date_format(published_date, '%Y-%m-%d')
from (
    select * from book
    where category = '경제'
) b
join author a
on b.author_id = a.author_id
order by published_date asc;