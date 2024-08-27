#diffrent ways to find out factorial of a number
def fact(n):
    if n<0:
        return 0
    elif n==0 or n==1:
        return 1
    else:
        f=1
        while(n>1):
            f*=n
            n-=1
        return f
num=5
print(fact(num))                    

#another way to findd factorial 
def factorial(n):
    #single line to find factorial of a given number
    return 1 if(n==0 or n==1) else n*factorial(n-1)

num=int(input('please enter numbeer to find the factorial: '))
print(f'factorial of number {num} is: {factorial(num)}')  

#third way to find the factorail of a given number
def facts(n):
    res=1
    for i in range(2,n):
        res=res*i
    return res  
n1=6    
print(f'factorial of number {n1} is: {facts(n1)}')       