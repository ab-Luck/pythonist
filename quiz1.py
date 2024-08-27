    
user=input('are u ready for test say yes,no,wait or y,n,w  ')
if user=='y':
    print()
    print(f'u entered: {user}')
    print()
    questions=('what is answer of this 2+1=?','what is answer of this 2x0=?','what is the name of capital of Pakistan?'
    ,'what is the capital  of china?')
    options=(('A: 2','B: 3','C: 1','D: 4'),('A: 2','B: 1','C: 0','D: None'),('A: Islamabad','B: Lahore','Karachi',
    'D: None'),('A: Bejing','B: Shanghai','C: Xinjiag','D: None'))

    answers=('B','C','A','A')
    counter=0
    guesses=[]
    guesses_correct=[]
    score=0

    for question in questions:
        print(question)
        for option in options[counter]:
            print(option)
    
        guess=input('select from (A,B,C,D) ').upper()
        guesses.append(guess)
        if guess==answers[counter]:
            score+=1
            guesses_correct.append(guess)
            print('Correct')
        
        else:
            print('Incorrect')
            print(f'{answers[counter]} is the correct answer')
        
        counter+=1
    print('--------------')
    print('    Results    ')
    print('--------------')
    score=score/len(questions)*100
    print(f"Your score is: {score}%")
    if score<60:
        print('you are not eligible for scholarships')
    else:
        print('Congratulations! u can avail this scholarship')   
    useres=input('do u want to get the summary of your result? say y for yes or n for no: ')
    if useres=='y':
        print('here is your summary!')
        print('----------------')    
        print('Answers: ',end='')
        for answer in answers:
            print(answer,end='')
        print()
        print('Guesses: ',end='')
        for guess in guesses:
            print(guess,end='')
        print()
        print('Your Correct Answers: ',end='')
        for g in guesses_correct:
            print(g,end='')
        
        else:
            ('Thanks for visiting us')

elif user=='w':
    print(f'u entered: {user}')
    print('u can come back later to attempt this test')
else:
    print(f'u entered: {user}')
    print('thanks for visiting')            


