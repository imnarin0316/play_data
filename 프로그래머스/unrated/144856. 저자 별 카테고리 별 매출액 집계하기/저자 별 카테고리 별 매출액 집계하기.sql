select  b.AUTHOR_ID
        , a.AUTHOR_NAME
        , b.CATEGORY
        , sum(b.PRICE * s.SALES) as TOTAL_SALES
from    BOOK_SALES s    join BOOK b on s.BOOK_ID = b.BOOK_ID
                        join AUTHOR a on b.AUTHOR_ID = a.AUTHOR_ID
where   s.SALES_DATE like '2022-01%'
group   by a.AUTHOR_NAME, b.CATEGORY
order   by 1, 3 desc

# SELECT AUTHOR.AUTHOR_ID, AUTHOR.AUTHOR_NAME, BOOK.CATEGORY, SUM(BOOK.PRICE * BOOK_SALES.SALES) AS TOTAL_SALES
# FROM BOOK_SALES
#     JOIN BOOK ON BOOK.BOOK_ID = BOOK_SALES.BOOK_ID
#     JOIN AUTHOR ON BOOK.AUTHOR_ID = AUTHOR.AUTHOR_ID
# WHERE BOOK_SALES.SALES_DATE LIKE "2022-01%"
# GROUP BY AUTHOR.AUTHOR_NAME, BOOK.CATEGORY
# ORDER BY AUTHOR.AUTHOR_ID ASC, BOOK.CATEGORY DESC;