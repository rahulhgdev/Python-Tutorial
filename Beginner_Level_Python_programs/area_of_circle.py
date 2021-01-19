
#Area = pi * r2
#where r is radius of circle 

def findArea(r): 
    PI = 3.142
    return PI * (r*r) 

num = int(input("Enter radius: "))
print("Area is %.6f" % findArea(num))