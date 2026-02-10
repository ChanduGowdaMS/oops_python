class Student:
    college_name = "ABC College"
    def __init__(self, name, roll_no):
        self.name=name
        self.roll_no=roll_no
    @classmethod
    def change_college(cls, new_name):
        cls.college_name=new_name
    @staticmethod
    def is_pass(marks):
        if marks>=35:
            return "Pass"
        else:
            return "Fail"
    def display(self, mark):
        print(self.name)    
        print(self.roll_no)    
        print(Student.college_name) 
        print(self.is_pass(mark))

obj=Student("chandu", 12)
obj.display(69)   
obj1=Student("gowda", 2)
obj1.display(34)   
Student.change_college("XYZ College")
