
def Perimetr(a,b):
    return int(2*a + 2*b),a,b
def Area(a,b):
    return int(a*b),a,b

def PrintPerimetr(P,a,b):
    print("The perimeter of the rectangle with sides "+ str(a) + " and " + str(b) + " is " +str(P) + ".")
def PrintArea(S,a,b):
    print("The area of the rectangle with sides " + str(a) + " and " + str(b) + " is " +str(S) + ".")

a = 3
a = int(a)
b = 4
b = int(b)
PrintPerimetr(Perimetr(a,b))
PrintArea(Area(3,4))
