import random
print( "welcom to rock paper scissors Game ")
user_score =0
comp_score =0
ties =0
name=input("enter your name:")

while "true":

    print(""" 
    wining rules:
      rock vs paper     --> paper wins
      paper vs scissors --> scissors wins
      rock vs scissors  --> rock wins
    """)
    print('''
    choices are:
    1. rock 
    2. paper
    3. scissors
    ''')
    print("It's your turn ")
    choice = int(input("enter your choice from 1-3:  "))
    while choice > 3 or choice < 1:
        choice= int(input("enter valid choice: "))
    
    if choice == 1:
        user_choice = "rock"
    elif choice == 2:
        user_choice = "paper"
    elif choice == 3:
        user_choice = "scissors"

    print("The user's choice is:", user_choice)
    print("Now it's a computer's turn")

    computer = random.randint(1,3)
    if computer == 1:
        comp_choice = "rock"
    elif computer == 2:
        comp_choice = "paper"
    elif computer == 3:
        comp_choice = "scissors"

    print("The computer's choice is:", comp_choice)

    if (user_choice == "paper" and comp_choice == "rock"):
        result = user_choice
        
    elif (user_choice == "rock" and comp_choice == "paper"):
        result = comp_choice
        
    elif (user_choice == "scissors" and comp_choice == "rock"):
        result = comp_choice
        
    elif (user_choice == "rock" and comp_choice == "scissors"):
        result = user_choice
        
    elif (user_choice == comp_choice):
        result = " "
        print("its Tie")
        
    elif (user_choice == "paper" and comp_choice == "scissors"):
        result = comp_choice
        
    elif (user_choice == "scissors" and comp_choice == "paper"):
        result = user_choice
    
    if result == user_choice:
        print(result,"wins")
        print("user Wins")
    elif result == comp_choice:
        print(result,"wins")
        print("comp Wins")
        
    if not input("Do you want to play again? (yes/no): ").lower() == 'yes':
        print("Game Over !")
        print("Thanks For Playing")
        running = "false"
        break