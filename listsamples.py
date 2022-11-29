list1=["apple","banana","ornage"]
list2=(("pinapple","1000"))
list1.extend(list2)

print(list1)

p1=list(("apple",2,10,100,"orange"))
p1[1:4]=["onion","pine","mango"]
p1.insert(0,"wow")
print(p1)
p1.insert(-2,"wow")
p1.remove("wow")
p1.pop(0)
print(p1)