
def nth_power(exponent ):
    def pow_of(base):
        return pow(base, exponent)
    return pow_of                           # note that we are returning function without function

square = nth_power(2)
print(square(31))
print(square(32))
print(square(33))
print(square(34))
print(square(35))
print(square(36))
print(square(37))
print(square(38))
print(square(39))

print('------')

cube = nth_power(3)
print(cube(2))
print(cube(3))
print(cube(4))
print(cube(5))
print(cube(6))
print(cube(7))
print(cube(8))
print(cube(9))