# select  *,count(*) 
# from    MEMBER_PROFILE m join REST_REVIEW r on m.MEMBER_ID = r.MEMBER_ID
# where   (select count(*) from REST_REVIEW group by MEMBER_ID order by 1 desc limit 1)
# group   by m.MEMBER_ID

SELECT  M.MEMBER_NAME
        , R.REVIEW_TEXT
        , DATE_FORMAT(R.REVIEW_DATE, '%Y-%m-%d') REVIEW_DATE
FROM    REST_REVIEW R INNER JOIN MEMBER_PROFILE M ON R.MEMBER_ID = M.MEMBER_ID
WHERE   R.MEMBER_ID = (SELECT MEMBER_ID
                     FROM REST_REVIEW
                     GROUP BY MEMBER_ID
                     ORDER BY COUNT(REVIEW_ID) DESC
                     LIMIT 1)
ORDER BY REVIEW_DATE, R.REVIEW_TEXT