# #find common elements in the list 
###################################
# l1=[22,'orange','apple','apple']
# l2=['apple','banana',22,22]
# cm=set(l1) 
# print(cm)
# cm1=set(l2)
# print(cm1)
# cm2=cm1&cm
# print(cm2)
###################################
#calculate average of a list
# list1=[12,34,56,78]
# a=sum(list1)/len(list1)
# print(a)
###################################
#generating a list of random numbers
#one method with list comprehension
# import random
# rand=[random.randint(1,50) for i in range(10)]
# print(rand)
###################################
#another wayy to make a random numbers list
import random
rand=[]
for i in range(15):
    rand.append(random.randint(1,50))
c=rand
print(f'original list created: {c}')
print()
c1=set(rand)
print(f'set delivered from that new created list: {c1}')

cc=len(c)
print(f'length of original list: {cc}')
cc1=len(c1)
print(f'length of set created by it: {cc1}')
print(f'original list has {cc-cc1} duplicate number')

