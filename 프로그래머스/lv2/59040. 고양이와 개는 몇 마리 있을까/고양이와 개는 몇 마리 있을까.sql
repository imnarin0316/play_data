select  ANIMAL_TYPE, count(*) as count
from    ANIMAL_INS
group   by ANIMAL_TYPE
order   by 1