x=lambda a : 5*a
print(x(3))

f=lambda s,v,b: s+v+b
print(f(3,100,99))



#double function
def my_fun(z):
    return lambda k: k*z

g=int(input("enter a number modifier :"))
modifier= my_fun(g)

print(modifier(9))
