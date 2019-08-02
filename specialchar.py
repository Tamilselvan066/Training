t=input()
a=0
for i in t:
	if i.isnumeric():
		pass
	elif i.isalpha():
		pass
	elif i.isspace():
		pass
	else:
		a+=1
print(a)
