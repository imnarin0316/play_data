# select  year(o.SALES_DATE) as YEAR
#         , month(o.SALES_DATE) as MONTH
#         , count(o.USER_ID) as PUCHASED_USERS 
#         , round(count(distinct o.USER_ID) / (select count(*) from USER_INFO where year(JOINED) = 2021) , 1) as PUCHASED_RATIO
# from    USER_INFO u join ONLINE_SALE o on u.USER_ID = o.USER_ID
# where   year(u.JOINED) = 2021
# group   by month(o.SALES_DATE)
# order   by 1, 2

SELECT  YEAR(B.SALES_DATE) YEAR,
        MONTH(B.SALES_DATE) MONTH,
        COUNT(DISTINCT B.USER_ID) PUCHASEDUSERS,
        ROUND(COUNT(DISTINCT B.USER_ID)/(SELECT COUNT(*) FROM USER_INFO 
        WHERE YEAR(JOINED) = '2021'),1) PUCHASEDRATIO
FROM    USER_INFO AS A LEFT JOIN ONLINE_SALE AS B ON A.USER_ID = B.USER_ID
WHERE   YEAR(A.JOINED) = '2021' AND B.SALES_DATE IS NOT NULL
GROUP   BY 1, 2
ORDER   BY 1, 2