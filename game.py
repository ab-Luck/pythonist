import random
win_num=random.randint(0,100)
num=int(input("guess number btw 1 & 100: "))
guess=1
game_over=False
while not game_over:
    if num==win_num:

        print(f"you win the game and u guessed it in {guess}times")
        game_over =True
    else:
        if num>win_num:
            print("number is too high")
        else:
            print("number is too low")
        guess+=1
        num=int(input("guess it again: "))            