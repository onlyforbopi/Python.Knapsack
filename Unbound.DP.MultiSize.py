DP, multiple size dimensions
Our original problem has two dimensions to 'size': weight and volume. We can create a python size object, that knows how to enumerate itself over its given dimensions, as well as perform logical and simple mathematical operations. With the use of the Size object, a correct solution to the given unbounded knapsack problem can be found by the following proceedure:

from knapsack_sizer import makesize
 
Size = makesize('wt vol')
 
items = [
    # NAME, (WT, VOL), VALUE   
    ('panacea', Size(3, 25), 3000),
    ('ichor', Size(2, 15), 1800),
    ('gold', Size(20, 2), 2500) ]
capacity = Size(250, 250)
 
def knapsack_unboundedmulti_dp(items, C):
    # order by max value per item size
    items = sorted(items, key=lambda item: item[VALUE]/abs(item[SIZE]), reverse=True)
 
    # Sack keeps track of max value so far as well as the count of each item in the sack
    zero, one = tuple(zip(*((0,1) for i in C)))
    sack = dict( (i, (0, [0 for i in items]))   # size -> (value, [item counts])
                 for i in C.range(C+one) )
 
    for i,item in enumerate(items):
        name, size, value = item
        for c in C.range(size, C+one):
            sackwithout = sack[c-size]  # previous max sack to try adding this item to
            trial = sackwithout[0] + value
            used = sackwithout[1][i]
            if sack[c][0] < trial:
                # old max sack with this added item is better
                sack[c] = (trial, sackwithout[1][:])
                sack[c][1][i] +=1   # use one more
 
    value, bagged = sack[C]
    numbagged = sum(bagged)
    size = sum((items[i][1]*n for i,n in enumerate(bagged)), zero)
    # convert to (iten, count) pairs) in name order
    bagged = sorted((items[i][NAME], n) for i,n in enumerate(bagged) if n)
 
    return value, size, numbagged, bagged
 
dp = knapsack_unboundedmulti_dp(items, capacity)
print(capacity, dp)
Sample output
The solution found is printed as:

Size(wt=250, vol=250) (54500, Size(247, 247), 20, [('gold', 11), ('panacea', 9)])
I.e. a choice of 20 items: 11 gold and 9 panacea, for a total value of 54500.