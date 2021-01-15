tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )
print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])

print('\n')
# Updating tuple
# you can not update since tuples are immutable
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# Following action is not valid for tuples

#tup1[0] = 100

# So let's create a new tuple as follows
tup3 = tup1 + tup2
print(tup3)


# Deleting Tuple

tup = ('physics', 'chemistry', 1997, 2000)
print(tup)
del tup
#print("After deleting tup : ")
#print(tup)

print('\n')

# length of tuple
tuple1, tuple2 = (123, 'xyz', 'zara'), (456, 'abc')
print("First tuple length : ", len(tuple1))
print("Second tuple length : ", len(tuple2))


'''
Difference between List and Tuple
1	Lists are mutable	           
    Tuple are immutable
2	Implication of iterations is Time-consuming	      
    Implication of iterations is comparatively Faster
3	The list is better for performing operations, such as insertion and deletion.	
    Tuple data type is appropriate for accessing the elements
4	Lists consume more memory	           
    Tuple consume less memory as compared to the list
5	Lists have several built-in methods	    
    Tuple does no have must built-in methods.
6	The unexpected changes and errors are more likely to occur	
    In tuple, it is hard to take place. 
'''

