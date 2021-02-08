def Perimeter(a, b):
    return int(2 * a + 2 * b)

def Area(a, b):
    return a * b

num = input().split(" ")
First = int(num[0])
Second = int(num[1])

print("The perimeter of the rectangle with sides %d and %d is %d." % (First, Second, Perimeter(First, Second)))
print("The area of the rectangle with sides %d and %d is %d." % (First, Second, Area(First, Second)))