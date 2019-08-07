t,b=input().split()
a=abs(len(b)-len(t))
for i in range(len(t)):
    if(len(b)==1 and b[i] in t):
        break
    if (t[i]!=b[i]):
        a=a+1
print(a)
