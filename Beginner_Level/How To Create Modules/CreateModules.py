
# module is nothing but a python file

#from dir import imp           --1st  u caan also use as in this line         # this code will auto appear after shifting the python file i.e. imp.py into new directory

# above same code function can done with simple way of 1 line which is below


import dir.imp as rahul           # as keyword for using short notation without as it was print((dir.imp.add(10,20)))

print((rahul.add(56, 15)))
print((rahul.mul(56, 15)))



# print((imp.add(56, 15)))                --1st
# print((imp.mul(46, 57)))                 --1st