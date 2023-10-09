class paranthesis:
    def __init__(self,str1):
        self.str1=str1
    def check(self):
       
        stack=[]
        dict={'(':')' , '{':'}' , '[':']'}
        for i in self.str1:
         if i in dict:
            stack.append(i)
         elif len(stack)==0 or dict[stack.pop()] !=i:
            return False
        return len(stack) == 0
p1=paranthesis("((())){}}}")
print(p1.check())    