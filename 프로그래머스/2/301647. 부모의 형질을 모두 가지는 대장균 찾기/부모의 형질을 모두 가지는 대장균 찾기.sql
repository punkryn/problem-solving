-- 코드를 작성해주세요
select 
    e.id,
    e.genotype,
    ee.genotype parent_genotype
from ecoli_data e
join ecoli_data ee
on e.parent_id = ee.id
where (e.genotype & ee.genotype) = ee.genotype
order by e.id;