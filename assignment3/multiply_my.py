import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line
i = 5
j = 5
k = 5
def mapper(record):
    mtx = record[0]
    row = record[1]
    col = record[2]
    val = record[3]
    if mtx == 'a':
      for k_c in range(0, k):
        #str1 = str(row) + " " + str(k_c)
	#str2 = mtx + " " + str(col) + " " + str( val)
        #print "str1 = ",str1
        #print "str2 = ",str2
        mr.emit_intermediate((row,k_c),(mtx, col, val))
    else:
      for i_c in range(0, i):
        #str1 = str(i_c)+" "+ str(col)
	#str2 = mtx+" "+str(row)+" "+str(val)  	
        #print "str1 = ",str1
        #print "str2 = ",str2
	mr.emit_intermediate((i_c,col),(mtx, row, val))

def reducer(key, list_of_values):
    total = 0
    val_a = 1;
    val_b = 1;
    for j_c in range(0,j):
      for val in list_of_values:
        if (val[0] == 'a' and j_c == val[1]):
          val_a = val[2]
        if (val[0] == 'b' and j_c == val[1]):
          val_b = val[2]
      total += val_a*val_b	

    mr.emit((key[0], key[1], total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
