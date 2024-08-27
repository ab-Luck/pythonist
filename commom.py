#combine a list of strings(with empty string delimitor)
w=['str','join','ing']
print(''.join(w))
t1={1,2,3,4,4,4}


print(t1)

d={(1,2):3}
print(d[(1,2)])
#getting duplicate values from the list
l=[1,2,3,1,16,34,3,45,6,7,89,90,0,99,34,34,667,78,99,76,5,544,33,22]
d=[]
ul=[]
li=[]
le=[]
lo=[]
c=0
c1=0
ls=[]
for i in l:
    

    if l.count(i) > 1:
        li.append(i)
    if i%2==0 :
        le.append(i)
        c+=1
       
    else:
        lo.append(i)
        c1+=1
  
            

    if i not in ul:
        ul.append(i)
       
    elif i not in d:
        d.append(i)
   


print( f'Even Number: {le} in this list we found: {c} even numbers') 
print(len(le))
print( f'Odd Number: {lo} in this list we found: {c1} odd numbers')         
print( f'Duplicate: {d}')    
print( f'Without duplicate: {ul}')
print(len(ul))
print( f'Duplicated Values: {li}')
print()
print(ls)


