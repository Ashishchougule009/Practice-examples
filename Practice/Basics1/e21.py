from  math import sqrt
def fun(a,b):
    hyp= sqrt(a**2+b**2)
    
    return hyp

a = float(input("Enter side a: "))

b = float(input("Enter side b: "))

print("hypptenuse of triangle is {}".format(fun(a,b)))