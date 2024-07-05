-- 코드를 입력하세요
SELECT fp.product_id, fp.product_name, fp.product_cd, fp.category, fp.price
from food_product fp
where fp.price = (select max(fpp.price) from food_product fpp);