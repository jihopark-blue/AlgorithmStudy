select joined.ANIMAL_ID, joined.out 'NAME'
from ( 
    select o.ANIMAL_ID, o.NAME AS 'out', i.NAME AS 'in'
    from ANIMAL_OUTS o
    left join 
    ANIMAL_INS i
    on i.ANIMAL_ID = o.ANIMAL_ID
    ) AS joined
where joined.in is NULL and joined.out is not NULL
order by joined.ANIMAL_ID;