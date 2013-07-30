select A.row_num, B.col_num, sum(A.value*B.value) 
from A, B
where B.row_num = A.col_num 
group by A.row_num, B.col_num;
