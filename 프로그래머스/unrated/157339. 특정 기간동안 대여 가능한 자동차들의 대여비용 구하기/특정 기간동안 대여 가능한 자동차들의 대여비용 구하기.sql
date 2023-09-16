# select  r.CAR_ID
#         , r.CAR_TYPE
#         , round(r.daily_fee * 30 * ((100 - p.discount_rate) / 100)) as FEE
# from    CAR_RENTAL_COMPANY_CAR r join CAR_RENTAL_COMPANY_DISCOUNT_PLAN p 
#         on r.CAR_TYPE = p.CAR_TYPE
# where   r.CAR_TYPE in ('세단', 'SUV')
#         and p.DURATION_TYPE = '30일 이상' 
#         and r.daily_fee * 30 * (1-(p.DISCOUNT_RATE/100)) >= 500000 
#         and r.daily_fee * 30 * (1-(p.DISCOUNT_RATE/100)) < 2000000
#         and r.CAR_ID in 
#             (select h.CAR_ID 
#             from CAR_RENTAL_COMPANY_RENTAL_HISTORY h 
#             where h.END_DATE < 20221101 )  
# group   by r.CAR_ID
# order   by r.daily_fee * 30 * (1-(p.DISCOUNT_RATE/100)) desc
#         , r.CAR_TYPE asc
#         , r.CAR_ID desc;
        
        
SELECT c.CAR_ID, c.CAR_TYPE, ROUND(c.DAILY_FEE*30*(1-d.DISCOUNT_RATE/100)) AS FEE
FROM CAR_RENTAL_COMPANY_CAR c, CAR_RENTAL_COMPANY_DISCOUNT_PLAN d
WHERE c.CAR_TYPE = d.CAR_TYPE
    AND c.CAR_TYPE IN ('세단', 'SUV') 
    AND d.DURATION_TYPE = '30일 이상'
    AND c.DAILY_FEE*30*(1-DISCOUNT_RATE/100) >= 500000 AND c.DAILY_FEE*30*(1-DISCOUNT_RATE/100) < 2000000
    AND NOT c.CAR_ID IN (
        SELECT h.CAR_ID 
        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY h       
        WHERE h.END_DATE >= 20221101)
GROUP BY c.CAR_ID
ORDER BY c.DAILY_FEE*30*(1-(DISCOUNT_RATE/100)) DESC, c.CAR_TYPE, c.CAR_ID DESC