# select  MONTH(START_DATE) as MONTH
#         , CAR_ID
#         , count(MONTH(START_DATE)) as RECORDS
# from    CAR_RENTAL_COMPANY_RENTAL_HISTORY
# where   START_DATE between '2022-08-01' and '2022-10-31'
# group   by car_id, MONTH(START_DATE)
# having  sum(count(*)) >= 5
# order   by 1, 2 desc

select  month(START_DATE) as MONTH
        , CAR_ID
        , count(*) as RECORDS
from    CAR_RENTAL_COMPANY_RENTAL_HISTORY
where   car_id in   (select  car_id 
                    from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
                    where   START_DATE between '2022-08-01' 
                    and '2022-10-31' 
                    group   by car_id  
                    having  count(*) >= 5) 
        and START_DATE between '2022-08-01' and '2022-10-31'
group   by car_id, month(START_DATE)
HAVING  COUNT(*) != 0 
order   by 1, 2 desc 

# select  car_id
# from    CAR_RENTAL_COMPANY_RENTAL_HISTORY
# where   START_DATE between '2022-08-01' and '2022-10-31'
# group   by car_id 
# having  count(*) >= 5

# SELECT MONTH(H.START_DATE) AS MONTH, H.CAR_ID, COUNT(*) AS RECORDS
# FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY AS H
# WHERE H.CAR_ID IN (SELECT HH.CAR_ID 
#                   FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY AS HH
#                   WHERE DATE_FORMAT(HH.START_DATE, '%Y-%m') BETWEEN "2022-08" AND "2022-10"
#                   GROUP BY HH.CAR_ID
#                   HAVING COUNT(*) >= 5)
#     AND DATE_FORMAT(H.START_DATE, '%Y-%m') BETWEEN "2022-08" AND "2022-10"

# GROUP BY MONTH, H.CAR_ID
# HAVING COUNT(*) != 0 
# ORDER BY MONTH ASC, CAR_ID DESC