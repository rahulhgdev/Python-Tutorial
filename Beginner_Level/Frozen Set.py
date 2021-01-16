Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Frozen Set
>>> numbers = [1,2,3,4,1,5,6,4,2,3]
>>> fs = frozenset(numbers)
>>> fs
frozenset({1, 2, 3, 4, 5, 6})
>>> fs.add(7)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    fs.add(7)
AttributeError: 'frozenset' object has no attribute 'add'
>>> 
>>> 
>>> 
>>> # some basic operation with set
>>> 
>>> x ={"a","b","c"}
>>> 
>>> "a" in x
True
>>> "g" in x
False
>>> for i in x:
	print(i)

	
a
c
b
>>> x
{'a', 'c', 'b'}
>>> y = {"a","h",g"}
     
SyntaxError: EOL while scanning string literal
>>> y = {"a","h","g"}
>>> x
{'a', 'c', 'b'}
>>> y
{'g', 'h', 'a'}
>>> # to find union
>>> x|y
{'g', 'c', 'a', 'b', 'h'}
>>> # to find intersection
>>> x&y
{'a'}
>>> # to find difference
>>> x-y
{'c', 'b'}
>>> # to find subset
>>> x<y
False
>>> x={"h","g"}
>>> x<y
True
>>> 