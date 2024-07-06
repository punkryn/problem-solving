WITH A as (
    select 
        year(os.sales_date) YEAR, 
        month(os.sales_date) MONTH, 
        ui.user_id users
    from user_info ui
    join online_sale os
    on ui.user_id = os.user_id
    where year(ui.joined) = 2021
    group by YEAR, MONTH, ui.user_id
)
SELECT 
    A.YEAR, 
    A.MONTH,
    count(A.users) PURCHASED_USERS,
    round(count(A.users) / (select count(*) cnt from user_info where year(joined) = 2021), 1) PURCHASED_RATIO
from A
group by A.YEAR, A.MONTH
order by A.YEAR, A.MONTH;

