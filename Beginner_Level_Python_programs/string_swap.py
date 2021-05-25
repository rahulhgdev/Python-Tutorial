s=input()
s=list(s)
res=""
for i in range(0,len(s)-1,2):
    temp=s[i+1]
    s[i+1]=s[i]
    s[i]=temp
print(res.join(s))
