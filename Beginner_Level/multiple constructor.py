

# IT ISN'T NOT POSSIBLE TO DECLARE MULTIPLE INIT METHOD IF U DECLARE MULTIPLE INIT MTHD THEN PYTHON WILL CONSIDERED LAST INIT METHOD AS MAIN AND PREVIOUS INIT METHOD IS OVERWRITTEN BY LAST INIT METHOD

class Hello:
    # def __init__(self):   pass     # it is an empty method
    # def __init__(self, name): pass
    # def __init__(self, *args, **kwargs): pass     #    -- 1st

   def __init__(self,name):
       self.name = name
       self.age = 10                         # it is possible to declare attributes without passing as arguments in the function


hello = Hello()
hello = Hello('name', 'age', name = 'chaman')              #    -- 1st