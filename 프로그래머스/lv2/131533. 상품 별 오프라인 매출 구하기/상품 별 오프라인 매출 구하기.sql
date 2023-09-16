select  p.PRODUCT_CODE
        , p.PRICE * sum(o.SALES_AMOUNT) as SALES
from    PRODUCT p join OFFLINE_SALE o on p.PRODUCT_ID = o.PRODUCT_ID
group   by o.PRODUCT_ID
order by 2  desc, 1

# select PRODUCT_ID, sum(SALES_AMOUNT)
# from    OFFLINE_SALE
# group by PRODUCT_ID
