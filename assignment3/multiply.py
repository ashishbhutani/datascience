
import MapReduce
import sys

mr = MapReduce.MapReduce()


# We assume that matrix dimensions is known beforehand
# A is MxK matrix, whereas B is KxN one
M = 5
K = 5
N = 5

def mapper(record):
    matrix, row, col, value = record
    
    for n in range(N):
        if matrix == 'a':
            destination_cell = (row,n)
            serial_number = col
        else:
            destination_cell = (n,col)
            serial_number = row
        mr.emit_intermediate( destination_cell, (matrix ,serial_number, value) )
            

def reducer(key, list_of_values):
    
    left_matrix_value = [ (item[1],item[2]) for item in list_of_values if item[0] == 'a' ]
    right_matrix_value = [ (item[1],item[2]) for item in list_of_values if item[0] == 'b' ]

    result = 0

    for item_L in left_matrix_value:
        for item_R in right_matrix_value:
            if item_L[0] == item_R[0] :
                result += item_L[1] * item_R[1]

    mr.emit( ( key[0], key[1], result ) )

inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
