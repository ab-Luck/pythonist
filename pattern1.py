#printing a bit complex patterns
#     *
#    **
#   ***
#  ****
# *****  
#now i will make a logic for it 
#simplest way to create a diamond pattern in python don't need to use extra inner loop
n=int(input('enter a desired number for pattern: '))
s=input('please enter a symbol u want to print:*,#,&.,% ')
for i in range(n-1):#in this outer loop if u put (n-1) then it will produce a exact diamond
    for j in range(n-i):
        print(' ',end='')
    for j in range(i+1):
        print(s,end=' ')  #'*'-->u can replace s with '*'
    print()    


for i in range(n):#i=0
    for j in range(i+1):#first printing all the spaces(decreasing triangle)
        print(' ',end='')  
    for j in range(n-i):#printing all the stars(increasing triangle)
        print(s,end=' ')#'*'-->u can replace s with '*'
      
    print()
