
class Cal:
    num =100
    def __init__(self,a,b):
        print("I am called automatically")
        self.a=a
        self.b=b

    def subti(self):

        print("Subraction step")
        return Cal.num -self.a - self.b
    def getdate(self):
        return Cal.num +self.a +self.b
        print("addition performed")


obj = Cal(10,20)
print(obj.a)
print(obj.b)
print(obj.subti())
obj.getdate()
