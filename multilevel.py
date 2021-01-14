"""Multiple Inheritance"""

#parent class
class Human():
    def __init__(self):
        super().__init__()
        print("inside human constructor")
        
    def walk(self):
        print("human can walk")
    
#first derived class
class Male(Human):
    def __init__(self):
        super().__init__()
        print("inside male constructor")
        
    def walk(self):
        print("male can walk")
        
#second derived class
class Female(Human):
    def __init__(self):
        super().__init__()
        print("inside female constructor")
        
    def walk(self):
        print("female can walk")  
        
#final child class
class Student(Female,Male):
    def __init__(self):
        super().__init__()
        print("inside student constructor.")
        
        
x = Student()

print(Student.__mro__)