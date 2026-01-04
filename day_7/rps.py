print("Let's play Rock, Paper, Scissors!")
vari1 = True
player_1 = input("You are player 1. Choose either Rock,Paper or Scissors:\n").lower()
player_2 = input("You are player 2. Choose either Rock,Paper or Scissors:\n").lower()
if player_1 != "rock" and player_1 != "paper" and player_1 != "scissors":
    print("Not a valid input for the first player.Please choose again.")
    player_1 = input("Choose either Rock,Paper or Scissors:\n").lower()

if player_2 != "rock" and player_2 != "paper" and player_2 != "scissors":
    print("Not a valid input for the second player.Please choose again.")
    player_2 = input("Choose either Rock,Paper or Scissors:\n").lower()
if (player_1 == "rock" and player_2 == "scissors") or (player_1 == "scissors" and player_2 == "paper") or (player_1 == "paper" and player_2 == "rock"):
    print(f'Player 1 has chosen {player_1} and Player 2 has chosen {player_2}. That means Player 1 has won the match.')
    vari1 = False
elif (player_2 == "rock" and player_1 == "scissors") or (player_2 == "scissors" and player_1 == "paper") or (player_2 == "paper" and player_1 == "rock"):
    print(f'Player 1 has chosen {player_1} and Player 2 has chosen {player_2}. That means Player 2 has won the match.')
    vari1 = False
elif player_1 == player_2:
    print(f'Player 1 has chosen {player_1} and Player 2 has chosen {player_2}. That means it is a tie. Please play again.')
    vari1 = True