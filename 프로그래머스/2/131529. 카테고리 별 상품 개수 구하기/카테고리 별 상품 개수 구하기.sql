-- 코드를 입력하세요
SELECT left(product_code, 2) cd, count(*)
from product
group by cd
order by cd;