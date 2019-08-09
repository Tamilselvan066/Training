num=list(input())
t=len(num)
for v in range(0,t,2):
    temp=num[v]
    num[v]=num[v+1]
    num[v+1]=temp
print("".join(num))
