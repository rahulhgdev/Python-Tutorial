Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> numbers = [1,2,3,4,5,6,7,8,9]
>>> even = []
>>> for i in numbers:
	if i%2==0:
		even.append(i)

		
>>> even
[2, 4, 6, 8]
>>> # syntax [output for-loop condition]
>>> even = [i for i in numbers if i%2==0]
>>> even
[2, 4, 6, 8]
>>> cube_numbers = [i*i*i for i in numbers]
>>> cube_numbers
[1, 8, 27, 64, 125, 216, 343, 512, 729]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> # Set Comprehension
>>> s = set{[1,2,3,4,5,2,3]}
SyntaxError: invalid syntax
>>> s = set([1,2,3,4,5,2,3])
>>> s
{1, 2, 3, 4, 5}
>>> type(s)
<class 'set'>
>>> even = { i for in s if i%2==0}
SyntaxError: invalid syntax
>>> even
[2, 4, 6, 8]
>>> 
>>> 
>>> 
>>> 
>>> # Dictionary Comprehension
>>> 
>>> cities = ["Mumbai","new york","tokyo"]
>>> country = ["India","USA","Japan"]
>>> z = zip(cities,country)
>>> z
<zip object at 0x00000253A2C7BF00>
>>> for a in z:
	print(a)

	
('Mumbai', 'India')
('new york', 'USA')
('tokyo', 'Japan')
>>> d = {city:country for city, country in zip(cities,country)}
>>> d
{'Mumbai': 'India', 'new york': 'USA', 'tokyo': 'Japan'}
>>> type(d)
<class 'dict'>
>>> dir(d)
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> 