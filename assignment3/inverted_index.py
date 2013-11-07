import MapReduce
import sys

"""
See Problem statement #1 in README
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    words = value.split()
    seen = {}
    for w in words:
      if (not seen.get(w,False)): 
        seen[w] = True
        mr.emit_intermediate(w, key)
#ram 1,1,1
def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    #total = 0
    #for v in list_of_values:
    #  total += v
    mr.emit((key, list_of_values))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
