# Brute force, single size attribute
# A brute-force solution for items with only one 'size' attribute would look like the following and would not scale:

from operator import itemgetter as iget
from itertools import product
from random import shuffle
 
NAME, SIZE, VALUE = range(3)
items = (
    # NAME, SIZE, VALUE
    ('A', 3, 2),
    ('B', 5, 4),
    ('C', 7, 6),
    ('D', 9, 8) )
capacity = 8
 
def knapsack_unbounded_enumeration(items, C):
 
    # find max of any one item
    max1 = [ int(C/item[SIZE]) for item in items ]
    itemsizes  = [ item[SIZE]  for item in items ]
    itemvalues = [ item[VALUE] for item in items ]
 
    #def totvalue(itemscount, =itemsizes, itemvalues=itemvalues, C=C):
    def totvalue(itemscount):
        nonlocal itemsizes, itemvalues, C
 
        totsize = sum( n*size for n, size in zip(itemscount, itemsizes) )
        totval  = sum( n*val  for n, val  in zip(itemscount, itemvalues) )
 
        return (totval, -totsize) if totsize <= C else (-1, 0)
 
    # Try all combinations of bounty items from 0 up to max1
    bagged = max( product(*[range(n+1) for n in max1]), key = totvalue )
    numbagged = sum(bagged)
    value, size = totvalue(bagged)
    size = -size
    # convert to (iten, count) pairs) in name order
    bagged = sorted((items[i][NAME], n) for i,n in enumerate(bagged) if n)
 
    return value, size, numbagged, bagged