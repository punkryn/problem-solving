-- 코드를 입력하세요
SELECT INGREDIENT_TYPE, SUM(total_order) TOTAL_ORDER
from first_half, icecream_info
where first_half.flavor = icecream_info.flavor
group by INGREDIENT_TYPE
order by TOTAL_ORDER asc;