#list1=[1,2,3,4]
#print(list(map(lambda item:item*item,list1)))
a={1:2,2:30,3:-4}
k=sorted(a.items,key=lambda x:x[1])
x=dict(k)
print(x)

