from fun2 import Cal


class ChildCal(Cal):
    num1=100
    def __init__(self):
        Cal.__init__(self,10,100)
    def multip(self):
        print("Multiplication performed")
        return self.getdate() * self.subti() * self.num1

p1=ChildCal()
print(p1.multip())