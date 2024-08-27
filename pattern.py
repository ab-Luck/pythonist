n=5
#very important: outer loop determines the rows and inner loop determines the column
for i in range(0,n):#1st iteration: i=0--2nd iter: i=1,i=2,i=3,i=4
    for j in range(0,i+1):#1st iteration: 0+1=1 ,,, 2nd:1+1=2,,3rd: 2+1=3 
        print('a', end='')
    print('\r')   
for i in range(n,0,-1):#i=0
    for j in range(0,i+0):#
        print('*', end='')
    print('\r')   

num=int(input('enter a desired number: '))  
#printing square pattern
def func(num):
    for i in range(num):#i=0
        for j in range(num):#j=0,j=1,j=2,j=3,j=4
            print('*',end=' ')
        print('\r')  
func(num)    

#new practice session(simplest way)

for i in range(n):#i=0
    for j in range(i+1):#i+1=0+1=1, i+1=1+1=2 so on
        print('*',end=' ')
    print()   

for i in range(n):#i=0
    for j in range(n-i):#(i,n)
        print('*',end=' ')
    print()         