with plan7 as (
    select discount_rate from CAR_RENTAL_COMPANY_DISCOUNT_PLAN
    where car_type = '트럭' and duration_type = '7일 이상'
), plan30 as (
    select discount_rate from CAR_RENTAL_COMPANY_DISCOUNT_PLAN
    where car_type = '트럭' and duration_type = '30일 이상'
), plan90 as (
    select discount_rate from CAR_RENTAL_COMPANY_DISCOUNT_PLAN
    where car_type = '트럭' and duration_type = '90일 이상'
)
SELECT
    history_id,
    floor((
        case
            when datediff(joined.end_date, joined.start_date) + 1 >= 90
                then (100 - plan90.discount_rate) / 100
            when datediff(joined.end_date, joined.start_date) + 1 >= 30
                then (100 - plan30.discount_rate) / 100
            when datediff(joined.end_date, joined.start_date) + 1 >= 7
                then (100 - plan7.discount_rate) / 100
            else
                1
        end
    ) * joined.daily_fee * (datediff(joined.end_date, joined.start_date) + 1)) FEE
from (
    select history.*, car.car_type, car.daily_fee
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY history
    join (
        select *
        from CAR_RENTAL_COMPANY_CAR
        where car_type = '트럭'
    ) car
    on history.car_id = car.car_id
) joined, plan7, plan30, plan90
order by FEE desc, history.history_id desc;