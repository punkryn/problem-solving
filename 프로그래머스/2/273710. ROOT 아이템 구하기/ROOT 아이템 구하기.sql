-- 코드를 작성해주세요
select info.item_id, info.item_name
from item_info info
join item_tree tree
on info.item_id = tree.item_id
where tree.parent_item_id is null
order by info.item_id asc;