class student:
    def __init__(self,student_class,student_name):
        self.student_class=student_class
        self.student_name=student_name
    def student_id(self):
        x=str(self.student_class)
        return self.student_name+x
student1=student(411,"PINAK")
print(student1.student_id())
        