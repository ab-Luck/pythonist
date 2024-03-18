questions=('what is answer of this 1+1=?','what is answer of this 1x1=?','what is answer of this 1-1=?')
options=(('A: 2','B: 3','C: 1','D: 4'),('A: 2','B: 0','C: 1','D: None'),('A: 1','B: 0','C: None','D: All'))

answers=('A','C','B')
guesses=[]
guess_correct=[]
score=0
question_num=0
for question in questions:
    print('-------------------------')
    print(question)
    for option in options[question_num]:
        print(option)
    
    guess=input('enter(A,B,C,D): ').upper()
    guesses.append(guess)
    if guess==answers[question_num]:
        score+=1
        guess_correct.append(guess)
        print('correct')
    else:
        print('incorrect')
        print(f'{answers[question_num]} is the correct answer')    
    question_num+=1
print('    Results    ')
print('----------------------------')
print('Answers: ',end='')
for answer in answers:
    print(answer,end='')
print()    

print('Guesses: ',end='')
for guess in guesses:
    print(guess,end='')
print()   

print('correct ones: ',end='')
for g in guess_correct:
    print(g,end='')
print()    

score=score/len(questions) * 100
print(f'Your score is {score}%')
