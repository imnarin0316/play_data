select  i.NAME, i.DATETIME
from    ANIMAL_INS i left join ANIMAL_OUTS o on i.ANIMAL_ID = o.ANIMAL_ID
where   o.DATETIME is null
order   by i.DATETIME 
limit   3