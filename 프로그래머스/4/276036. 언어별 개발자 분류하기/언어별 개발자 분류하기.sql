-- 풀이
-- skillcodes : 개발자들이 사용하는 프로그래밍 언어에 대한 정보를 담은 테이블
-- developers : 개발자들의 프로그래밍 스킬 정보를 담은 테이블
-- developers 테이블에서 grade별 개발자의 정보를 조회하려고 함
-- A : Front + Python
-- B : C#
-- C : 그 외 Front
with skills as (
    select d.id, s.name, s.category
    from developers d, skillcodes s
    where d.skill_code & s.code > 0
), front as (
    select distinct(id)
    from skills
    where category = 'Front End'
), python as (
    select distinct(id)
    from skills
    where name = 'Python'
), grade_a as (
    select distinct(a.id)
    from front a, python b
    where a.id = b.id
), grade_b as (
    select distinct(id)
    from skills
    where id not in (
        select *
        from grade_a
    ) and name = 'C#'
), grade_c as (
    select distinct(id)
    from skills
    where id not in (
        select *
        from grade_a
        union
        select *
        from grade_b
    ) and category = 'Front End'
), temp as (
    select 'A' as grade, id
    from grade_a
    union all
    select 'B' as grade, id
    from grade_b
    union all
    select 'C' as grade, id
    from grade_c
)

select t.grade, t.id, d.email
from temp t, developers d
where t.id = d.id
order by 1, 2