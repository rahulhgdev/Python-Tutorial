list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];

print('\n')

print(list1)
print(list2)

print('\n')

print("list1[0]: ", list1[0])
print(list1[-1])   #last element in list
print("list2[1:5]: ", list2[1:5])

print('\n')

#updating list2
list2[2] = 2001;
print("list2[2]: ", list2[2])
print(list2)

print('\n')

#apend, delete and insert

aList = [123, 'xyz', 'zara', 'abc'];
print("Before appending",   aList)
aList.append( 2009 );                                           #add element at last
print("after appending : ", aList)

print('\n')

del_list = ['lamborghini','ferrari','mercedes-benz','audi','gtr']
print(del_list)
del del_list                                                    #deleting dl_list
#print(del_list)

print('\n')

insert_lst = ['butter','khari','toast','jeera-khari']
print("Before inserting element at index 2",insert_lst)
insert_lst.insert(2,'tuti-fruty-toast')                         #inserting element in list
print("after inserting element at index 2",insert_lst)


print('\n')

# concating  2 lists

lst1 = [11,22,33,44,55]
lst2 = [66,77,88,99,100]
list_concat = lst1 + lst2
print(list_concat)

#lst1 + 120       #it'll give error bcoz in python we can't add elements in  this way without index

print('\n')

print(len(list_concat))                       #length of list

print('\n')
# for no in list_concat:
#     if no == 66:
#         continue
#     print(no)

# in operator to check whether element exists of not

print(11 in list_concat)