-- 코드를 입력하세요
SELECT p.product_code, sum(p.price * os.sales_amount) sales
from offline_sale os, product p
where os.product_id = p.product_id
group by p.product_code
order by sales desc, p.product_code asc;