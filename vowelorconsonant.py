t=input()
if(t>='a' and t<='z'):
    l=['a','e','i','o','u']
    if t in l:
        print('Vowel')
    else:
        print('Consonant')
else:
    print('Invalid')
