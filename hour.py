t=[]
a=[]
for i in range(2):
	x1,y1=map(int,input().split())
	t.append(x1)
	a.append(y1)
print(abs(t[0]-t[1]),abs(a[0]-a[1]),sep=' ')
