select  u.USER_ID, u.NICKNAME, sum(b.PRICE) as TOTAL_SALES
from    USED_GOODS_BOARD b left join USED_GOODS_USER u 
        on b.WRITER_ID = u.USER_ID
where   b.STATUS = 'DONE'
group   by b.WRITER_ID
having  sum(b.PRICE) >= 700000
order   by 3