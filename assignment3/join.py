import MapReduce
import sys

"""
See Problem statement #2 in README
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    #key = record[0]
    #value = record[1]
    col_id = record[1]
    #for w in words:
    mr.emit_intermediate(col_id, record)

def reducer(col_id, list_of_record):
    # key: word
    # value: list of list
    order_record = []
    for record  in list_of_record:
      if (record[0] == "order"):
        order_record = record
	break

    for record in list_of_record:
      if (record[0] == "order"):
        continue
      new_record = order_record + record 	
      mr.emit(new_record)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
