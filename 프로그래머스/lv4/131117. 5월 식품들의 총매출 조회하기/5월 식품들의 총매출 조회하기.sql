# select p.PRODUCT_ID, p.PRODUCT_NAME, (p.PRICE * o.AMOUNT as TOTAL_SALES
# from   FOOD_PRODUCT p join  FOOD_ORDER o on p.PRODUCT_ID = o.PRODUCT_ID
# where   o.PRODUCE_DATE like '2022-05%'
# group   by o.PRODUCT_ID
# order   by p.PRICE * o.AMOUNT desc, p.PRODUCT_ID

select o.PRODUCT_ID, p.PRODUCT_NAME,  sum(o.AMOUNT) * p.PRICE as TOTAL_SALES
from FOOD_ORDER o join FOOD_PRODUCT p on o.PRODUCT_ID = p.PRODUCT_ID
where   o.PRODUCE_DATE like '2022-05%'
group   by o.PRODUCT_ID
order   by sum(o.AMOUNT) * p.PRICE desc, o.PRODUCT_ID