Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> basket = {"apple","mango","orange","pear","banana","apple"}
>>> basket
{'apple', 'pear', 'banana', 'orange', 'mango'}
>>> a = set()
>>> a.add(11)
>>> a.add(22)
>>> a.add(33)
>>> a.add(44)
>>> a
{33, 11, 44, 22}
>>> # don't initialize empty set bcoz python consider it set dictionary
>>> b = {}
>>> type(b)
<class 'dict'>
>>> b = {'somrthing'}
>>> b
{'somrthing'}
>>> type(b)
<class 'set'>
>>> # since set is unordered that means you can't access using index
>>> basket[0]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    basket[0]
TypeError: 'set' object is not subscriptable
>>> 
>>> 
>>> 
>>> 
>>> # creating set from list by passing list as argument in constructor of set
>>> numbers = [1,2,3,4,5,2,1,3,5]
>>> set_numbers = set(numbers)
>>> set_numbers
{1, 2, 3, 4, 5}
>>> set_numbers.add(6)
>>> set_numbers
{1, 2, 3, 4, 5, 6}
>>> 