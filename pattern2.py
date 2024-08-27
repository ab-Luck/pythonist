#creating a butterfly pattern 
n=5
for i in range(n):
    
    print('*'*i,end='')
   
    print(' '*(n-i)*2,end='')

      
    print('*'*i)    

for i in range(n,0,-1):
    print('*'*i,end='')
   
    print(' '*(n-i)*2,end='')

      
    print('*'*i)    