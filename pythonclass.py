class person():
    def __init__(self,name,age):
        self.name=name;
        self.age=age;
    def __str__(self):
        return f"{self.name}({self.age})"
    def name_fun(self):
        print("first name:",self.name,(self.age))
p=person("sjj",32)
print(p)

print(p.name)
print(p.age)
p.name="shilpa"
p.age=30

p.name_fun()