# Decorators wrap a function and modify its behaviour in one way or the another without having to directly change the source code of the function being decorated.

def decorator_X(func):
    def wrapper_func():
        print('X' * 20)
        func()
        print('X' * 20)

    return wrapper_func()

def decorator_Y(func):
    def wrapper_func():
        print('Y' * 20)
        func()
        print('Y' * 20)

    return wrapper_func                # RETURN WITHOUT PARANTHESIS

    # @decorator_func                                             # --1st

@decorator_X                        # --2ND
@decorator_Y
def say_hello():
    print('Hello World')


# hello = decorator_func(say_hello())       # this is same as --1st
# hello = decorator_Y(decorator_X(say_hello))                 # --2ND
# hello()

