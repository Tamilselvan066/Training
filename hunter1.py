try:
	num=int(input())
	array=list(map(int,input().split()))
	ta=[]
	for i in array:
		if array.count(i)>1:
			if i not in ta:
				ta.append(i)
	print(*ta)
	if len(ta)==0:
		print("unique")
except ValueError:
	print("invalid")
