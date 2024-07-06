-- 코드를 입력하세요
SELECT date_format(sales_date, '%Y-%m-%d') sd, product_id, user_id, sales_amount
from online_sale
where month(sales_date) = 3 and year(sales_date) = 2022
union all (
    select
    date_format(sales_date, '%Y-%m-%d'), product_id, null USER_ID, sales_amount
    from offline_sale ofs
    where month(sales_date) = 3 and year(sales_date) = 2022
)
order by sd asc, product_id asc, user_id asc;