select count(*) from (select distinct docid from frequency where docid in (select docid from frequency where term ="transactions" ) and docid in (select docid from frequency where term = "world"));
