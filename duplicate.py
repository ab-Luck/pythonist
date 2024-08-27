#checking the duplicate numbeers in the list 
lis=[1,23,4,56,7,89,0,12,3,56,8,1,1,4,57,9,0]
ul=[]
dl=[]
for l in lis:
    if l not in ul:
        ul.append(l)
    elif l not in dl:
        dl.append(l)
print(ul)
print(dl)   

#using count method to find out the duplicate numbers from the list
new=[]
new1=[]
for l in lis:
    c=lis.count(l)
    print(f'numbers repeated {c} times')
    if c>1:
        new1.append(l)
        if new.count(l)==0:
            new.append(l)
print(new)
print(new1)
#to find out the frequency of a items in a list(to check how many times the same items are repeating)
from collections import Counter
f=Counter(lis)
print(f'frequency of items in a list: {f}')