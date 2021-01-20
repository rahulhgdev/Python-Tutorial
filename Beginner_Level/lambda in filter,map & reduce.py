
# Lambda Functions is also known as Anonymous function bcoz they don't have any name some tym they also called oneline function bcoz they written in oneline of code
# function returning from function thats where lambda function are used

from functools import reduce

# def double(x):
#     return x*2
#
# def add(x,y):
#     return x+y
#
# def pro(x,y,z):
#     return x*y*z


# Lambda function of above functions

double = lambda x : x * 2
add = lambda x, y : x + y
pro = lambda x, y, z : x * y * z

print(double(10))
print(add(10,20))
print(pro(10,20,30))

# map, filter, reduce

my_list1 = [2,5,8,10,9,3]
my_list2 = [1,4,7,8,5,1]

a = map(lambda x : x * 2, my_list1)
print(list(a))                           # u must to cast list otherwise it will give wierd hexadecimal instead of list

b = map(lambda  x, y : x + y, my_list1 , my_list2)
print(list(b))

# filter function gives boolean value and it take function as 1st argument

c= filter(lambda x : x%2 ==0, my_list1)
print(list(c))

d= filter(lambda x :  True if x > 5  else False, my_list1)          # using if else inside filter
print(list(d))

# to use reduce we have import functool at the top

e = reduce(lambda x, y : x+y, my_list1)
print(e)