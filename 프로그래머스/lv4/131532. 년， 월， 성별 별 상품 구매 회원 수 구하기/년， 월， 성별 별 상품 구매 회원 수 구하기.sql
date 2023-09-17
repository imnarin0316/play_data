select  year(s.SALES_DATE) as YEAR
        , month(s.SALES_DATE) as MONTH
        , i.GENDER
        , count(distinct s.USER_ID) as USERS
from    USER_INFO i join ONLINE_SALE s on i.USER_ID = s.USER_ID
where   i.GENDER is not null
group   by year(s.SALES_DATE), month(s.SALES_DATE), i.GENDER
order   by 1,2,3