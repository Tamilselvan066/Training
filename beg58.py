t,a=map(int,input().split())
num=list(map(int,input().split()))[:t]
count=0
for x in range (0,t):
  if a==num[x]:
    count+=1
if count==0:
  print('no')
else:
  print('yes') 
