select  b.BOOK_ID
        , a.AUTHOR_NAME
        , date_format(b.PUBLISHED_DATE, '%Y-%m-%d') as PUBLISHED_DATE
from    BOOK b join AUTHOR a on b.AUTHOR_ID = a.AUTHOR_ID
where   b.CATEGORY = '경제'
order   by b.PUBLISHED_DATE 
