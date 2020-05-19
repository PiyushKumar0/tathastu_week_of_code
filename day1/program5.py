#https://www.linkedin.com/in/piyushkumar0

player1 = int(input("Enter the runs scored by player 1 in 60 balls: "))
player2 = int(input("Enter the runs scored by player 2 in 60 balls: "))
player3 = int(input("Enter the runs scored by player 3 in 60 balls: "))

strikerate1 = player1 * 100 / 60
strikerate2 = player2 * 100 / 60
strikerate3 = player3 * 100 / 60

print("\nStrike rate of player 1 is", strikerate1)
print("Strike rate of player 2 is", strikerate2)
print("Strike rate of player 3 is", strikerate3)

print("Runs scored by player 1 if they played 60 more balls is", player1 * 2)
print("Runs scored by player 2 if they played 60 more balls is", player2 * 2)
print("Runs scored by player 3 if they played 60 more balls is", player3 * 2)

print("Maximum number of sixes player 1 could hit:", player1 // 6)
print("Maximum number of sixes player 2 could hit:", player2 // 6)
print("Maximum number of sixes player 3 could hit:", player3 // 6)
