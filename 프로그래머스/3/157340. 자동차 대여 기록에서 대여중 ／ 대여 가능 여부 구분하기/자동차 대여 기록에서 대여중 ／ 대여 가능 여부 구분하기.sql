-- 코드를 입력하세요
select car_id, (
    case
        when s = 0
            then '대여 가능'
        else
            '대여중'
    end
) availability
from (SELECT car_id, sum(
    case
        when '2022-10-16' between start_date and end_date
            then 1
        else
            0
    end
) s
from car_rental_company_rental_history
GROUP BY car_id) A
order by car_id desc;