import random, sys

print("ROCK, PAPER, SCISSORS")

win = 0
loses = 0
tie = 0

while True:
    print(f"Wins = {win} Loses = {loses} Ties = {tie}\nEnter your move: (r)ock, (p)aper, (s)cissors, or (q)uit.")
    while True:
        player_choice = input()
        random_number = random.randint(1,3)
        
        if player_choice == 'q':
            sys.exit()
        elif player_choice == 'r' or player_choice == 'p' or player_choice == 's':
            break
        print("Type either r, p, s, or q.")

    if random_number == 1:
        computer_choice = 'r'
    elif random_number == 2:
        computer_choice = 'p'
    elif random_number == 3:
        computer_choice = 's'
    
    if player_choice == computer_choice:
        print("TIE! Go again.")
        tie = tie + 1
    elif player_choice == 'r' and computer_choice == 's':
        print("Computer chose SCISSORS. You win!")
        win = win + 1
    elif player_choice == 's' and computer_choice == 'p':
        print("Computer chose PAPER. You win!")
        win = win + 1
    elif player_choice == 'p' and computer_choice == 'r':
        print("Computer chose ROCK. You win!")
        win = win + 1
    elif computer_choice == 'r' and player_choice == 's':
        print("Computer chose ROCK. You lose!")
        loses = loses + 1
    elif computer_choice == 's' and player_choice == 'p':
        print("Computer chose SCISSORS. You lose!")
        loses = loses + 1
    elif computer_choice == 'p' and player_choice == 'r':
        print("Computer chose PAPER. You lose!")
        loses = loses + 1


