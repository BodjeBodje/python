"""_summary_
    object: An object is anything of interest that data is stored about:
        a phone, a person,desk, a electronic
        
    
"""
# a=10
# b="boy"

# print(type(a))
# print(type(b))

#ec2 blueprint
class Ec2:
    def __init__(self,name:str,image:str):
        self.name=name
        self.image=image
        self.ip="12.12.12.4"
        
    def stop(self):
        print("stopping")
    def start(self):
        print("Starting")
    def checkingMetric(self):
        print("Checking metric for ec2 instance")
#Create an object of type ec2
instance1=Ec2(name="class24-ec2",image="ubuntu")

print(type(instance1))
print(instance1.name,instance1.image,instance1.ip)
instance1.checkingMetric()
instance1.start()
instance1.stop()
        

class Student:
    def __init__(self,student_id:str,grade:str,attendance_days:int):
        self.student_id=student_id
        self.grade=grade
        self.attendance_days=attendance_days
    def isPromoted(self):
        promoted=self.attendance_days>10
        print(f"Promoted status{promoted}")
        return promoted
    
#create an object
student1=Student(student_id="1",grade="B", attendance_days=25)
student2=Student(student_id="2",grade="C", attendance_days=5)

student1.isPromoted()
student2.isPromoted()

#blueprint
print("===========================")
class Man:
    def __init__(self,name:str,legs:int,hands:int,head:int):
        self.__name=name
        self.__legs=legs
        self.__hands=hands
        self.__head=head
        
        #methods
    def think(self):
        print(f"{self.__name} is thinking using his {self.__head} head(s)")
    def run(self):
        print(f"{self.__name} is running using his {self.__legs} leg(s)")
    def pick(self):
        print(f"{self.__name} is picking using his {self.__hands} hand(s)")
        
    #getters & setters
    def getName(self):
        return self.__name
    def setName(self,name: str):
        self.__name=name
    def getLegs(self):
        return self.__legs
    def setLegs(self,number:int):
        self.__legs=number

# amadou=Man(name="Amadou",legs=2,hands=2,head=1)

# amadou.run()
# amadou.think()
# amadou.pick()
# print(type(amadou))

#
class Animal:
    
    def run(self):
        print("The animal running")
    def walk(self):
        print("The animal is walking")
        
class Cat(Animal):
    def meow(self):
        print("meow")
        
class Dog(Animal):
    def bark(self):
        print("bark")

dog1=Dog()
dog1.run()
# dog1.walk()
# dog1.bark()

# cat1=Cat()
# cat1.run()
# cat1.walk()
# cat1.meow()

print("==========================review class and inherit")

class Bouria:
    def __init__(self,habitant:str, case:str,arbre:str):
        self.habitant=habitant
        self.case=case
        self.arbre=arbre
    def genre(self):
        print("Genre test")
village=Bouria(habitant="Man", case="house",arbre="Orange")
village.genre()