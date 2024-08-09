select 
    DATE_FORMAT(DATETIME, '%H') AS HOUR,
    COUNT(*) AS COUNT
from ANIMAL_OUTS    
where DATE_FORMAT(DATETIME, '%H') between '09' and '20'
group by HOUR
order by HOUR;