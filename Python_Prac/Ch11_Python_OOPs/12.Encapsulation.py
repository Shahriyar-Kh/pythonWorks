#Example 1
class Student:
    def __init__(self,name="Shary",marks=50,age=24):
        self.name=name
        self.__age=age
        self._marks=marks
    
    def studentData(self):
        print("Name: {} age: {} marks: {} ".format(self.name,self.__age,self._marks))
        
obJ1=Student()
obj2=Student("Umair",300,20)
obJ1.studentData()
obj2.studentData()


print(f"\nName: {obj2.name}")#public access in anywhere 
print(f"Marks: {obj2._marks}")#protected access in out of class but not access out of package
#print(f"Age: {obj2.__age}") not Access out of class

#Private data access
print(obj2._Student__age)