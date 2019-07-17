tt = int(input())
aa = list(map(int,input().split()[:tt]))
mm = sorted(aa)
for i in mm:
    print(i,end=" ")
