#loop through lists
names=['abrar','kamran','arslan','muzzamil']
#loop without index
for name in names:
    print(name.title())
#loop with index
for name in range(len(names)):
    print(names[name])
#loop with index and value
for name,nam in enumerate(names):
    print(name,nam)   

#loop through multiple lists
l=[12,34,56]
l1=[33,66,99]
l2=[14,28,56]    
for x,y,z in zip(l,l1,l2):
    print(x,y,z)
