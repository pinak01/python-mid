from datetime import date

class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob
    
    def calc_age(self):
        today = date.today()
        age = today.year - self.dob.year
        
        if today < date(today.year, self.dob.month, self.dob.day):
            age -= 1
        
        return age

person1 = Person('pinak', 'India', date(2005, 9, 17))
print(person1.calc_age())


    

    
        