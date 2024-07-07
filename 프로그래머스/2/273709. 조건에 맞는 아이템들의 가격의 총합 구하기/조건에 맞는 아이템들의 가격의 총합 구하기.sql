select 
    sum(price) total_price
from item_info
where rarity = 'LEGEND'
group by rarity;