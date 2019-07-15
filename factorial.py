nos=int(input())
fact=1
if nos==0:
    print(fact)
else:
    for i in range(2,nos+1):
        fact*=i
    print(fact)
