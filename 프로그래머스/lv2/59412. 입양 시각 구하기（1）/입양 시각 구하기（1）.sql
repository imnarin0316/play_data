select  hour(DATETIME) as HOUR
        , count(*) as COUNT
from    ANIMAL_OUTS
where  hour(DATETIME) between 09 and 19
group   by hour(DATETIME)
order   by 1