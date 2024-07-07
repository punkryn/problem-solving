-- 코드를 입력하세요
SELECT
    user_id,
    nickname,
    concat_ws(' ', city, street_address1, street_address2) 전체주소,
    concat_ws('-', left(tlno, 3), substring(tlno, 4, 4), right(tlno, 4)) 전화번호
from (
    select writer_id from used_goods_board
    group by writer_id
    having count(*) >= 3
) board
join used_goods_user usr
on board.writer_id = usr.user_id
order by usr.user_id desc;