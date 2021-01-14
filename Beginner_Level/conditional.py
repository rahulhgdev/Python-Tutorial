'''   If Statement
Syntax:-
if expression:
   statement(s) '''
print('\n\t\t if expression\n')
var1 = 100
if var1:
   print("1 - Got a true expression value")
   print(var1)

var2 = 0
if var2:
   print("2 - Got a true expression value")
   print(var2)
print("Good bye!")


#if-else expression
#Syntax:-
#if expression:
#   statement(s)
#else:
#   statement(s)
print('\n\t\t if-else expression\n')

num = input("Enter a number: ")
num=int(num)
if num%2==0:
   print("number is even")
else:
   print("number is odd")


'''  nested if-else expression
Syntax:-
if expression1:
   statement(s)
   if expression2:
      statement(s)
   elif expression3:
      statement(s)
   elif expression4:
      statement(s)
   else:
      statement(s)
else:
   statement(s) '''
print('\n\t\t nested-if-else expression\n')
var = 100
if var < 200:
   print("Expression value is less than 200")
   if var == 150:
      print("Which is 150")
   elif var == 100:
      print ("Which is 100")
   elif var == 50:
      print ("Which is 50")
   elif var < 50:
      print ("Expression value is less than 50")
else:
   print ("Could not find true expression")

print ("Good bye!")

print('\n\t\t more on if-else\n')

indian = ['samosa','dal-chawal','matar-panir']
chinese = ['fried-rice','chicken-triple-rice','manchurian-soup']
italian = ['pizza','pasta','risotto']

dish = input("Enter a dish name: ")
if dish in indian:
   print("Kehte hai hamko pyar se India Wale")
elif dish in chinese:
   print("China corona")
elif dish in italian:
   print("italian de pasta de africa de dombivali")
else:
   print('dish not found create your own dish')