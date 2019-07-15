tam=int(input())
if tam>1:
   for i in range(2,tam):
      if tam%i==0:
         print("no")
         break
   else:
        print("yes")
else:
  print("no")
