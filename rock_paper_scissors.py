# Allows 2 players to play rock, paper, scissors as many times as they wish. It tracks each player's wins and the 
# number of draws.
def determineWinner(player1, player2):
    global draws
    global player1_wins
    global player2_wins
    if player1 == player2:
        draws += 1
        return print(f"It's a draw. Player 1 has {player1_wins} wins, Player 2 has {player2_wins} wins, and there are {draws} draws.")
    elif (player1 == "r" and player2 == "s") or (player1 == "s" and player2 == "p") or (player1 == "p" and player2 == "r"):
        player1_wins += 1
        return print(f"Player 1 wins. Player 1 has {player1_wins} wins, Player 2 has {player2_wins} wins , and there are {draws} draws.")
    elif player1 == "s" and player2 == "r" or (player1 == "p" and player2 == "s") or (player1 == "r" and player2 == "p"):
        player2_wins += 1
        return print(f"Player 2 wins. Player 1 has {player1_wins} wins, Player 2 has {player2_wins} wins, and there are {draws} draws.")
    
play_again = 'y'
draws = 0
player1_wins = 0
player2_wins = 0

while play_again == 'y':
    player1 = input("Player 1: Type 'r' for rock, 'p' for paper, or 's' for scissors: ")
    while player1 not in ('r', 'p', 's'): player1 = input("Player 1: Type 'r' for rock, 'p' for paper, or 's' for scissors: ")
    player2 = input("Player 2: Type 'r' for rock, 'p' for paper, or 's' for scissors: ")
    while player2 not in ('r', 'p', 's'): player2 = input("Player 2: Type 'r' for rock, 'p' for paper, or 's' for scissors: ")
    determineWinner(player1, player2)
    play_again = input("Would you like to play again? (y/n): ")
    if play_again not in ('y', 'n'): play_again = input("Would you like to play again? (y/n): ")