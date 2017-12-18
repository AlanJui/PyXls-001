# create a 2d list with fixed values (static allocation)
from IPython.utils.py3compat import xrange

a = [ [ 2, 3, 4 ] , [ 5, 6, 7 ] ]
print(a)

"""
Dynamic Allocation
"""

#=========================================================
# Create a variable-sized 2d list
#=========================================================
# (1) Append each row
rows = 3
cols = 2

a=[]
for row in xrange(rows):
    a += [[0]*cols]

print("This IS ok.  At first:")
print("   a = {}".format(a))

#--------------------------------------------------------
a[0][0] = 42
print("And now see what happens after a[0][0]=42")
print("   a = {}".format(a))

#=========================================================
# (2) Use a 2D List

def make_2d_list(rows, cols):
    a = [ ]
    for row in xrange(rows):
        a += [ [ 0 ] * cols ]
    return a


rows = 3
cols = 2
a = make_2d_list(rows, cols)
print("This IS ok.  At first:")
print("   a = {}".format(a))

a[ 0 ][ 0 ] = 42
print("And now see what happens after a[0][0]=42")
print("   a = {}".format(a))

#=========================================================
# (3) Use a list comprehension

rows = 3
cols = 2
a = [ ([0] * cols) for row in xrange(rows) ]
print("This IS ok.  At first:")
print("   a = {}".format(a))

a[ 0 ][ 0 ] = 42
print("And now see what happens after a[0][0]=42")
print("   a = {}".format(a))
