t,s=list(map(int,input().split()))
ts=0
for i in range(t,s+1):
    if i>1:
        for x in range(2,i):
            if(i%x==0):
                break
        else:
            ts+=1
print(ts)
