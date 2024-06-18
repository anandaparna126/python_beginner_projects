import random
l = ["rock", "paper", "scissor"]
while True:
    ccount=0
    ucount=0
    user_choice = int(input('''
                            Game Start.....
                            1 Yes | Play
                            2 No | Exit                      
                            '''))
    if user_choice==1:
        for a in range(1, 6):
            user_input = int(input('''
                                    1 Rock
                                    2 Paper
                                    3 Scissor
                                    '''))
            if user_input==1:
                uchoice="rock"
            elif user_input==2:
                uchoice="paper"
            elif user_input==3:
                uchoice="scissor"
            Comp_choice = random.choice(l)
            if Comp_choice==uchoice:
                print("You choosed:", uchoice)
                print("Computer choosed:",Comp_choice)
                print("Game Draw")
                ucount=ucount+1
                ccount=ccount+1
            elif (Comp_choice=="scissor" and uchoice=="rock") or (Comp_choice=="rock" and uchoice=="paper") or (Comp_choice=="paper" and uchoice=="scissor"):
                print("You choosed:", uchoice)
                print("Computer choosed:",Comp_choice)
                print("You Win")
                ucount=ucount+1
            else:
                print("You choosed:", uchoice)
                print("Computer choosed:",Comp_choice)
                print("Computer Win")
                ccount=ccount+1
        print("===============")
        print("====RESULT=====")        
        if ccount == ucount:
            print("MATCH DRAW!!")
            print("User Score: ",ucount)
            print("Computer Score: ",ccount)
        elif ucount > ccount:
            print("YOU WIN THE GAME!!")
            print("User Score: ",ucount)
            print("Computer Score: ",ccount)
        else:
            print("COMPUTER WIN THE GAME!!")
            print("User Score: ",ucount)
            print("Computer Score: ",ccount)
    else:
        break