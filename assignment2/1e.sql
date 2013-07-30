select count(*) from (select docid, SUM(count) as total_cnt  from frequency group by docid having SUM(count) >300);
