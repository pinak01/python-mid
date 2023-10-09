class unique:
    def __init__(self,list):
        self.list=list
    def subset(self):
        l=[]
        k=[]
        x=self.list.copy()
        for i in range(0,len(x)):
          
            for j in range(i,len(x)+1):
                l.append(x[i:j])
        for i in l:
            if i:
                k.append(i)
        return k
list1=unique([1,2,3,4])
print(list1.subset())

