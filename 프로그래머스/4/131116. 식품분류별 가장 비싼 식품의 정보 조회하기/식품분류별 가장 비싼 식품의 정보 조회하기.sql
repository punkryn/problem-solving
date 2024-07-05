select f.category, f.price, f.product_name
from food_product f
join (
    select category, max(price) price
    from food_product
    where category in ('과자', '국', '김치', '식용유')
    group by category
) fp on f.category = fp.category
where f.price = fp.price
order by f.price desc;

