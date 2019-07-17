t=input()
a=t.lstrip('-').replace('.','',1).isdigit()
if(a==True):
	print("yes")
else:
	print("No")
