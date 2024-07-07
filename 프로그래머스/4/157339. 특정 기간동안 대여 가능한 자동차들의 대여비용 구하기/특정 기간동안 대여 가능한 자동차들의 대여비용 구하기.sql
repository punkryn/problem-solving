select 
    car.CAR_ID, 
    car.CAR_TYPE,
    floor(30 * car.daily_fee * (100 - plan.discount_rate) / 100) FEE
from (
    select car_id, car_type, daily_fee
    from CAR_RENTAL_COMPANY_CAR
    where car_id in (
        select car_id
        from CAR_RENTAL_COMPANY_RENTAL_HISTORY
        group by car_id
        having max(end_date) < '2022-11-01'
    ) 
    and (CAR_TYPE = '세단' or CAR_TYPE = 'SUV')
) car
join CAR_RENTAL_COMPANY_DISCOUNT_PLAN plan
on plan.CAR_TYPE = car.CAR_TYPE and plan.duration_type = '30일 이상'
where 500000 <= floor(30 * car.daily_fee * (100 - plan.discount_rate) / 100)
and floor(30 * car.daily_fee * (100 - plan.discount_rate) / 100) < 2000000
order by FEE desc, CAR_TYPE asc, CAR_ID desc;