-- 코드를 입력하세요
SELECT COUNT(*) as USERS
FROM USER_INFO 
WHERE YEAR(JOINED) = 2021 AND (AGE BETWEEN 20 AND 29)