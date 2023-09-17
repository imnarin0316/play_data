select  CAR_ID
        , case  
            when max('2022-10-16' between start_date and end_date) then '대여중'
            else '대여 가능'
            end as AVAILABILITY
from    CAR_RENTAL_COMPANY_RENTAL_HISTORY
group by car_id
order   by 1 desc



# select  *
#         # , max(history_id)
# from    CAR_RENTAL_COMPANY_RENTAL_HISTORY  
# # group   by car_id
# order   by car_id