class student:
    def __init__(self,first,last,id_num):
        self.first=first
        self.last=last
        self.id_num=id_num
    def display(self):
        print("Name:",self.first + self.last)
        print("ID:",self.id_num)
class grade(student):
    def __init__(self,first,last,id_num,score):
        super().__init__(first,last,id_num)
        self.score=score
        super().display()
    def grade1(self):
        avg=sum(self.score)/len(self.score)
        if avg>=90 and avg<=100:
            return "GRADE: A"
        elif avg>=80 and avg<90:
            return "GRADE: B"
        elif avg>=60 and avg<80:
            return "GRADE: C"
        elif avg>=40 and avg<60:
            return "GRADE: D"
        elif avg<40:
            return "GRADE: F"
student1=grade("Pinak","Debnath","23BCE1253",[90,90,95,90,90])
print(student1.grade1())


