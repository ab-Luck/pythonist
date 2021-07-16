import random
win_num=random.randint(0,100)
guess_count=1
enter_num=input("guess a number b/w 1 and 100: ")
game_finish=False
while not game_finish :
    if int(enter_num)==win_num:
        print(f"u win the game and u guess it in {guess_count} times ")
        game_finish=True
        print("congrats....")    
    else:
        if int(enter_num )>40 and int(enter_num)<44:
            print("number is too close")
        elif int(enter_num )<win_num:
            print("number is too low")
        else:
            print("number is too high ")
        guess_count+=1      
        enter_num=int(input("guess it again:"))
    #print("congrats...")        
    
