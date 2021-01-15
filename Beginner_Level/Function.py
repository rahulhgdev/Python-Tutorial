def calculateTotal(exp):
    total = 0
    for item in exp:
        total = total + item
    return total

manoj_exp = [2100,3650,9812]
vishal_exp = [1230,3234,1245]

manoj_total = calculateTotal(manoj_exp)
vishal_total = calculateTotal(vishal_exp)

print("Manoj Total Expense:",manoj_total)
print("Vishal Total Expense:",vishal_total)

print('\n')

# another example

def sum(a,b):
    print("a:",a)
    print("b:",b)

    total = a+b
    print("total inside function:",total)
    return total
n = sum(5,6)
print("total outside function:",n)

print('\n')

# default argument

def printinfo( name, age = 35 ):

   print("Name: ", name)
   print("Age ", age)
   #return

printinfo( age=50, name="miki" )
printinfo( name="miki" )

print('\n')

# arguments are two type
#1) Positional Argument 2) Named Arguments


# Global and Local Variable

total = 0;      # Global variable

def sum(a,b):
    print("a:",a)
    print("b:",b)

    total = a+b             # local variable
    print("total inside function: i.e local variable",total)
    return total

n = sum(b=8,a=12)
print("total outside function: i.e global variable",total)

print('\n')

# defualt variable

def mul(a,b=0):
    print("a:",a)
    print("b:",b)

    multiplication = a * b
    print("multiplication inside function:",multiplication)
    return multiplication

m=mul(5)   # passed only 1 argument
print("Multiplication outside function:",m)

print('\n')

# Document string for explaining purpose of variables

def mul(a,b=0):
    print("a:",a)
    print("b:",b)
    """
    This function takes two arguments which are integer numbers and
    it will return multiplication of them as an output
    :param a:
    :param b:
    :return
    """

    multiplication = a * b
    print("multiplication inside function:",multiplication)
    return multiplication

m=mul(5,5154)   # passed only 1 argument
print("Multiplication outside function:",m)
