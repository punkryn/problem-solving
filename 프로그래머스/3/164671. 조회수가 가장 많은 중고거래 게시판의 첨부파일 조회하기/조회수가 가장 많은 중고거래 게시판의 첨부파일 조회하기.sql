-- 코드를 입력하세요
SELECT
    concat_ws('/', '/home/grep/src', board.board_id, concat(file.file_id, file.file_name, file.file_ext)) FILE_PATH
from used_goods_file file
join (
    select board_id
    from used_goods_board
    order by views desc
    limit 1
) board
on file.board_id = board.board_id
order by file.file_id desc;