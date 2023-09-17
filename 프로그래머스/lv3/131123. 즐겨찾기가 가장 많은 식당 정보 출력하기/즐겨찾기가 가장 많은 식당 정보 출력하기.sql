select  FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
from    REST_INFO
where   FAVORITES in (select max(FAVORITES) from REST_INFO group by FOOD_TYPE)
group   by FOOD_TYPE
order   by 1 desc