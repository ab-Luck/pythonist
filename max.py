#different ways to find out max numbers 
#method 1
a=2
b=4
if a>b:
    print('a is greater than b ',a)
else:
    print('b is greater than a ',b)    
#method 2
def Max(a,b):
    if a>b:
        return True
    else:
        return False
print(Max(12,11))        

#method 3
a=23
b=44
print(max(a,b))

#method 4
lis=[12,23,45,21]
lis.sort()
print(lis[-1])
print(lis)
