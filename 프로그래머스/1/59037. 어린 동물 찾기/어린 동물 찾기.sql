-- 코드를 입력하세요
SELECT animal_id, name
FROM animal_ins
WHERE intake_condition <> 'Aged'
ORDER BY animal_id

-- 풀이
-- 1. 젊은 동물 필터링
-- 2. 젊은 동물의 아이디와 이름 조회하기
-- 3. 결과는 아이디 순으로 조회하기