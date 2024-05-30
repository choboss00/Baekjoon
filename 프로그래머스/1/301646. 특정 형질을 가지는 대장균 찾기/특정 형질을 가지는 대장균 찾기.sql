-- 코드를 작성해주세요
select count(*) as count
from ecoli_data
where (genotype & 2 = 0) and ((genotype & 1 = 1) or (genotype & 4 = 4))