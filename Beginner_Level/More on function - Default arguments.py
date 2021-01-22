
# Deualt arguments *args and *kwargs


#def student(name = 'unknown name', age = 0):              --1st


def student(name, age, **marks): #*marks):  # u can use double Asterix to declare key value pair # provide this type i.e. marks at the last so it can readable easily   # USING METRIX IN FRONT OF ARGUMENTS IN PYHTON MEANS U CAN PROVIDE MULTIPLE ARGUMENTS

    print("name : ", name)
    print('age : ', age )
    print('marks :', marks)



# u can use for loop with marks even



#student()   # defuallt values when u don't provide values     -- 1st


student('rahul', 18,cs= 196, physics = 80, che =  74,maths =  67,english =  61, evs =  46) # whenever u use double asterix then it will print in the form of dictionary  # IT WILL PRINT IN THE FORM OF TUPPLES
