class Superlist(list):
    def __init__(self,l):
         self.l=l
    
   
          
lit1=Superlist([1,2])
print(len(lit1))
lit1.append([6,8,9])
print(lit1)