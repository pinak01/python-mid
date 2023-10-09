from functools import reduce
l1=[1,2,3,4]
def accumulator(acc,item):
    print(acc,item)
    return acc+item
print(reduce(accumulator,l1,0))