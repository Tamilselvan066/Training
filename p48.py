t = int(input())
a = list(map(int,input().split()[:t]))
avg = 0
for i in a:
    avg = i+avg
print(int(avg/t))    
