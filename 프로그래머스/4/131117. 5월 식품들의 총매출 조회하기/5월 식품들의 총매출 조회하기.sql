-- 코드를 입력하세요
SELECT pr.product_id, pr.product_name, sum(pr.price * ord.amount) total_sales
from food_product pr, food_order ord
where pr.product_id = ord.product_id
and year(ord.produce_date) = 2022
and month(ord.produce_date) = 5
group by pr.product_id
order by total_sales desc, pr.product_id asc;