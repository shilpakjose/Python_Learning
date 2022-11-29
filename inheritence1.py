#Create a class named Person, with firstname and lastname properties, and a printname method:

class person():
    def __init__(self,fname,lname):
        self.fname= fname
        self.lname=lname
    def printname(self):
        print("full name :",self.fname, self.lname)
p1 =person("shilpa","jose")

p1.printname()

#creating child class student and inherting properties from person

class student(person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.year =year
    def welcome(self):
        print("welcome",self.fname,self.lname,"to the year:", self.year)


x= student("Adam","Francis",2021)
x.printname()
x.welcome()
print(x.year)
