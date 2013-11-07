import MapReduce
import sys

"""
See Problem statement #5 in README
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    seq_id = record[0]
    dna_str = record[1]
    dna_str = dna_str[:-10]
    mr.emit_intermediate(dna_str,1)

def reducer(dna_str,dummy):
    mr.emit(dna_str)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
