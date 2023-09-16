# 7월 아이스크림 총 주문량과 상반기의 아이스크림 총 주문량을 더한 값이 큰 순서대로 상위 3개의 맛을 조회하는 SQL 문을 작성해주세요.

select  h.FLAVOR
# select  h.FLAVOR, sum(h.TOTAL_ORDER + j.TOTAL_ORDER) 
from    FIRST_HALF h left join JULY j on h.FLAVOR = j.FLAVOR
group   by h.FLAVOR
order   by sum(h.TOTAL_ORDER + j.TOTAL_ORDER) desc
limit   3