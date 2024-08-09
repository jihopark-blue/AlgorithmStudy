select U.USER_ID, U.NICKNAME, 
    concat(U.CITY, ' ', U.STREET_ADDRESS1, ' ', U.STREET_ADDRESS2) 전체주소,
    concat(substring(U.TLNO, 1, 3),
           '-',
           substring(U.TLNO, 4, 4),
           '-',
           substring(U.TLNO, 8, 4)
           ) 전화번호
    
from USED_GOODS_BOARD B
join USED_GOODS_USER U
on B.WRITER_ID = U.USER_ID
group by B.WRITER_ID
having count(B.WRITER_ID) >= 3
order by U.USER_ID DESC;