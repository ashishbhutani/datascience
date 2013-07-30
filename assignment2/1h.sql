SELECT C.value
from

(
SELECT
    A.docid as doc1,
    B.docid as doc2,
    SUM(a.[count] * b.[count] ) AS value
from
    frequency A
    join frequency B on A.term=B.term
where A.docid = '10080_txt_crude' and B.docid = '17035_txt_earn'
group by
    A.docid,
    B.docid
) C
;
