class calculator:
    def __init__(self,number1,number2):
        self.number1=number1
        self.number2=number2
    def sum(self):
        return self.number1+self.number2
    def multiply(self):
        return self.number1*self.number2
    def divide(self):
        return self.number1//self.number2
calc1=calculator(20,2)
print(calc1.sum())
print(calc1.multiply())
print(calc1.divide())
