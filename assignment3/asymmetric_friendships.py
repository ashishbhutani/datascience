import MapReduce
import sys

"""
See Problem statement #4 in README
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    person_name = record[0]
    frnd_name = record[1]
    if (person_name > frnd_name):
      mr.emit_intermediate((person_name, frnd_name),1)
    else:	
      mr.emit_intermediate((frnd_name, person_name),1)

def reducer(key, list_of_frns):
    length = len(list_of_frns)
    if (length == 1):
      mr.emit((key[0], key[1]))
      mr.emit((key[1], key[0]))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
