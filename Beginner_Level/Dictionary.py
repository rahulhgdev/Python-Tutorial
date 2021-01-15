# Each key is separated from its value by a colon (:), the items are separated by commas, and the whole thing is enclosed in curly braces.
# An empty dictionary without any items is written with just two curly braces, like this: {}.


dist = {"Mumbai":400001, "Delhi": 100001, "Chennai": 600001, "Kolkata": 700001}
print("Before Adding Pune:",dist)
print(dist["Delhi"])   #accessing using key

dist["Pune"] = 412000  #adding another key-value
print("After Adding Pune:",dist)

print('\n')

#Printing key-value pair method 1
for pincode in dist:
    print("Ciyt:",pincode,", Pincode:",dist[pincode])

print('\n')

#Printing key-value pair method 2

for k,v in dist.items():
    print("City:",k,"Pincode:",v)

print('\n')


# Deleting element with key
dist1 = {'Dog':'Bho-Bho','Cat':'Meow','Cow':'Bhoooo'}
print("Before:",dist1)
del dist1['Cat']
print("After:",dist1)

print('\n')


# Deleting whole dictionary
dist1 = {'Dog':'Bho-Bho','Cat':'Meow','Cow':'Bhoooo'}
print(dist1)
#del dist1
#print(dist1)

print('Dog' in dist1)   #check and return bool value either true or false
dist1.clear();
print(dist1)
print('\n')