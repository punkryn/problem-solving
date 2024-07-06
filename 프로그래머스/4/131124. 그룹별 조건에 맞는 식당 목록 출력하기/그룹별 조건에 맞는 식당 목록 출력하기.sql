-- 코드를 입력하세요
select mp.member_name, rr.review_text, date_format(rr.review_date, '%Y-%m-%d') REVIEW_DATE
from rest_review rr
join (SELECT count(member_id) cnt, member_id
from rest_review
group by member_id
order by cnt desc
limit 1) max_review_member
on rr.member_id = max_review_member.member_id
join member_profile mp
on max_review_member.member_id = mp.member_id
order by rr.review_date asc, rr.review_text asc;