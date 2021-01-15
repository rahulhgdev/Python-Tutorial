# writing to file

f= open("E:\\Python\\Beginner_Level\\file.txt","w")
f.write("I love Programming")
f.close()

print('\n')

# appending to file

f= open("E:\\Python\\Beginner_Level\\file.txt","a")
f.write("\nI love Coffee")
f.close()

print('\n')

# Reading file

f= open("E:\\Python\\Beginner_Level\\read.txt","r")
print(f.read())
f.close()

print('\n')

f= open("E:\\Python\\Beginner_Level\\read.txt","r")
for line in f:
    print(line)                     # see difference from above program
f.close()

print('\n')

# split() will split string using input character and return a list(array) of words
# to count words in a line
#
# f_out= open("E:\\Python\\Beginner_Level\\wordcount.txt","w")
# for line in f:
#     tokens = line.split(' ')
#     f_out.write("wordcout:"+str(len(tokens)) + line)
# f_out.close()

# with statement - for those forget to close files

with open("E:\\Python\\Beginner_Level\\wordcount.txt","r") as f:
    print(f.read())
print(f.closed)   # to check whether file is closed or not