# nested function u can define function inside a fucntion

# closures are sometimes uses in the placeof classes which usually have only one method or few method . Closures are highly used in decorators   

def outterFunction(text):
    def innerFunction():
        print(text)
    return  innerFunction     # to make closure fucntion from nested function you have to return function without paranthesis

a = outterFunction("Hello")
del outterFunction
a()                      # after deleting outterfunction o/p - Hello means a variable is sotring some spaces for innerfunction even outterfunction is deleted this is magic of 'closure'