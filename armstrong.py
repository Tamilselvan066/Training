nos=input()
s=0
for i in range(len(nos)):
   s+=pow(int(nos[i]),3)
if str(s)==nos:
  print("yes")
else: 
  print("no")
