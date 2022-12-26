-- 코드를 입력하세요
SELECT book.category, sum(bs.sales) from book 
join (select book_id, sales_date, sales from book_sales where year(sales_date) = 2022 and month(sales_date) = 1) as bs 
on book.book_id = bs.book_id
group by book.category
order by book.category;