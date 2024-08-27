#print out a multiplication table of your own choice

#i will ask user for his desired multiplication table 
user_input=int(input('Enter a number for which you want a multiplication table! '))
for num in range(1,11):
    print(num,'X',user_input,'=',num*user_input)