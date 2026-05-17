p1 = input("Player 1: ")
p2 = input("Player 2: ")

if p1 == p2:
    print("Tie")
elif p1 == "rock":
    if p2 == "scissors":
        print("Player 1 wins")
    else:
        print("Player 2 wins")
elif p1 == "paper":
    if p2 == "rock":
        print("Player 1 wins")
    else:
        print("Player 2 wins")
else:
    if p2 == "paper":
        print("Player 1 wins")
    else:
        print("Player 2 wins")
