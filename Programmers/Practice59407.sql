-- https://programmers.co.kr/learn/courses/30/lessons/59407
-- 이름이 있는 동물의 아이디

-- 코드를 입력하세요
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NOT NAME IS NULL
ORDER BY ANIMAL_ID ASC
