t=int(input())
count=0
while(t>0):
  dig=t%10
  count+=dig
  t=t//10
print(count)
