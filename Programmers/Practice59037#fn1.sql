-- https://programmers.co.kr/learn/courses/30/lessons/59037#fn1
-- 어린 동물 찾기

-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION != 'Aged';
