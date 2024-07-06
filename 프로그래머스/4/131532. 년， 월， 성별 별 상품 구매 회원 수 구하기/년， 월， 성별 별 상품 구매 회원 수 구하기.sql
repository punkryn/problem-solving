# -- 코드를 입력하세요
SELECT year(sales_date) YEAR, month(sales_date) MONTH, ui.gender GENDER, count(DISTINCT os.user_id) USERS
from online_sale os, user_info ui
where os.user_id = ui.user_id
and ui.gender is not null
group by YEAR, MONTH, GENDER
order by YEAR, MONTH, GENDER;