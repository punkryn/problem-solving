-- 코드를 입력하세요
SELECT usr.user_id, usr.nickname, board.total_sales
from (
    select writer_id, sum(price) total_sales
    from used_goods_board
    where status = 'DONE'
    group by writer_id
    having total_sales >= 700000
) board
join used_goods_user usr
on board.writer_id = usr.user_id
order by board.total_sales;