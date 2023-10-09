class SumFinder:
    def __init__(self, lst, target):
        self.lst = lst
        self.target = target

    def find(self):
        x = self.lst.copy()
        for i in range(0, len(x)-1):
            
                if x[i] + x[i+1] == self.target:
                    return f"{i+1}, {i+2}"
        return None

l1 = SumFinder([10, 20, 10, 40, 50, 60, 70], 50)
result = l1.find()
print(result)