-- 코드를 입력하세요
SELECT car.CAR_ID
from CAR_RENTAL_COMPANY_CAR car
where car_id in (
    select car_id from CAR_RENTAL_COMPANY_RENTAL_HISTORY history
    where month(start_date) = 10
) and car_type = '세단'
order by car.car_id desc;
