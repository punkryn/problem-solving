select month(start_date) MONTH, car_id, count(*) RECORDS
from car_rental_company_rental_history
where start_date between '2022-08-01' and '2022-10-31'
and car_id in (
    select car_id from car_rental_company_rental_history
    where start_date between '2022-08-01' and '2022-10-31'
    group by car_id
    having count(*) >= 5
)
group by MONTH, car_id
order by MONTH asc, car_id desc;