-- 코드를 입력하세요
SELECT info.rest_id, info.rest_name, info.food_type, info.favorites, info.address, round(avg(rev.review_score), 2) as avg_score
from rest_info info, rest_review rev
where info.rest_id = rev.rest_id
and left(info.address, 2) = '서울'
group by info.rest_id
order by avg_score desc, info.favorites desc;
