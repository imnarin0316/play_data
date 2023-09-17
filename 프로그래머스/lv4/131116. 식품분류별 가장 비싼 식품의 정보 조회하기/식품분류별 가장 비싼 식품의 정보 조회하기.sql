select  CATEGORY 
        , max(PRICE) as MAX_PRICE
        , PRODUCT_NAME
from    FOOD_PRODUCT
where   CATEGORY in ( '과자', '국', '김치', '식용유')
and     PRICE in (
        select  max(price)
        from    FOOD_PRODUCT 
        where   CATEGORY in ( '과자', '국', '김치', '식용유')
        group by CATEGORY 
        order by PRICE desc
        )  
group   by CATEGORY
order   by 2 desc


# select  max(price)
# from    FOOD_PRODUCT 
# where   CATEGORY in ( '과자', '국', '김치', '식용유')
# group by CATEGORY 
# order by PRICE desc