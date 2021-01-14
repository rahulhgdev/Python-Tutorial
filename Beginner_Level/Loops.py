''' while loop
Syntax:-
while expression:
   statement(s)
'''

var = 1
while var<=5:
    print(var*var)
    var +=1

print('\n')
#another example

count = 0
while (count < 9):
   print('The count is:', count)
   count = count + 1


print('\n\t\t For Loop \n')


''' for loop
syntax:-
for iterating_var in sequence:
   statements(s)
'''

#break & continue

for i in range(1,6):
    if i%2==0:
        continue
    print(i*i)
print('\n')


#another example
exp = [2340,2500,2780,1866]
total = 0
for item in exp:
    total = total+item
print("total expense:",total)
print("\n")

#another example

exp_1 = [2340,1560,1980,6520]
total_1 = 0
for i in range(len(exp_1)):
    print('Month:', (i+1), 'Expense', exp_1[i])
    total_1 = total_1 + exp_1[i]

print('Total expense is: ', total_1)
print('\n')

#another example

money_lost_location = 'golden park'
location = ['beturkar pada','chikan ghar','golden park','kala talao']
for i in location:
    if i == money_lost_location:
        print('money found on road of ',i)
        break
    else:
        print("money not found on road of",i)

# break and continue

