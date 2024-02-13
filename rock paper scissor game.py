import random                     # python in-built module import for print random number

computer = ["rock" , "scissors" , "paper"]     

computer_choice = random.choice(computer)       # choice choose 1 elements from computer

player_choice = input ("select 1 choice ->  rock or scissors or paper " ).lower()      # player option & finally will change lower case 



if player_choice in computer:       # this condition check player_choice in computer

    
    if player_choice == computer_choice:
        print("Match Tied!")                        # if both choice each match tied
        
        
    elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "scissors" and computer_choice == "paper") or        # player winning match conditions
        (player_choice == "paper" and computer_choice == "rock")
    ):    
        print("You Won The Match!")
        

    else:                                  # computer winning match statement
        print( "Computer Won!" )        

else:
    print( "Invalid Choice. Select correct choice.." )            # reselect statement

