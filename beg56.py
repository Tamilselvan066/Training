t=(input())
a=len(t)
count=0
sum1=0
for x in range (a):
  if (t[x].isdigit()):
    count=count+1
  elif(t[x].isalpha()):
    sum1=sum1+1
if(count!=0 and sum1!=0):    
  print('Yes')
else:
  print('No')  
