-- 코드를 입력하세요
SELECT PT_NAME, PT_NO, GEND_CD, AGE, IFNULL(TLNO, 'NONE') AS TLNO
FROM PATIENT
WHERE AGE <= 12 AND GEND_CD = 'W'
ORDER BY AGE DESC, PT_NAME ASC

-- PT_NO : 환자 번호
-- PT_NAME : 환자이름
-- GEND_CD : 성별코드
-- AGE : 나이
-- TLNO : 전화번호