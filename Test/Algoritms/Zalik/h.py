def Perimetr(a,b):
    return int(2*a + 2*b)
def Area(a,b):
    return int(a*b)

def PrintPerimetr(a):
    print("The perimeter of the rectangle with sides 3 and 4 is "+str(a)+".")
def PrintArea(a):
    print("The area of the rectangle with sides 3 and 4 is "+str(a)+".")

a = input("enter a")
a = int(a)
b = input("enter B")
b = int(b)
PrintPerimetr(Perimetr(3,4))
PrintArea(Area(3,4))