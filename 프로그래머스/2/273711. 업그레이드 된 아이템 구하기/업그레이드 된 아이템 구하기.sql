-- 코드를 작성해주세요
select info.item_id, info.item_name, info.rarity
from item_info info
join item_tree tree
on info.item_id = tree.item_id
where tree.parent_item_id in (
    select item_id
    from item_info
    where rarity = 'RARE'
)
order by info.item_id desc;