
def decorator_divide(func):
    def wrapper_func(a,b):
        print('divide', a, ' and ', b)
        if b == 0:
            print("Division With Zero Not Alloawed Dusra Positive Number Daal ")
            return
        return a / b
    return wrapper_func                             # RETURN WITHOUT PARANTHESIS


@decorator_divide
def divide(x,y):
    return x/y

print(divide(15,0))