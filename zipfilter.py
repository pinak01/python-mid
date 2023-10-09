l1=[1,2,3]
l2=[30,40,50 ]
def odd(item):
    return item%2!=0
print(list(zip(l1,l2)))
print(list(filter(odd,l1)))