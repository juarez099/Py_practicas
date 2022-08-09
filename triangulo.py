import math

'''Area y perimetro de un triangulo'''
a= float(input("Digita valor de a: "))
b= float(input("Digita valor de b: "))
c= float(input("Digita valor de c: "))
s=((a+b+c)/2)
def Perimetro(a,b,c):
    return a + b + c

def Semiperimetro(a,b,c):
    return ((a+b+c)/2)

def Area(a,b,c):
    A=math.sqrt((s*(s-a)*(s-b)*(s-c)))
    return round(A,3)

print(f"El perimetro es: {Perimetro(a,b,c)}")
print(f"El Semiperimetro es: {Semiperimetro(a,b,c)}")
print(f"El Area es: {Area(a,b,c)}")



