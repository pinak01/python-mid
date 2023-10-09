class datastructure:
    def __init__(self,list):
        
        self.list=list
    def enqueue(self,item):
       
        self.list.append(item)
        return self.list
    def dequeue(self):
        if not self.empty():
         return self.list.pop(0)
        else:
            return "Cannot remove elements"
    def empty(self):
        if len(self.list)==0:
            return True
data1=datastructure([20,30,40,50])
print(data1.enqueue(60))
print(data1.dequeue())
print(data1.enqueue(80))

