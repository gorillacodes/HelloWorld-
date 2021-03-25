from random import randint

print ("Stone = 1\nPaper = 2\nScissors = 3\n")

u_score = 0
c_score = 0

def game():
    
    u_input = int(input("Your move? "))

    c_input = randint(1, 4)

    if u_input == c_input:
        print("Tie")

    elif u_input == 1 and c_input == 2:
        print("Computer showed Paper \nComputer won")
        c_score += 1

    elif u_input == 1 and c_input == 3:
        print("Computer showed Scissors \nYou won")
        u_score += 1

    elif u_input == 2 and c_input == 1:
        print("Computer showed Stone \nYou won")
        u_score += 1

    elif u_input == 2 and c_input == 3:
        print("Computer showed Scissors \nComputer won")
        c_score += 1

    elif u_input == 3 and c_input == 1:
        print("Computer showed Stone \nComputer won")
        c_score += 1

    elif u_input == 3 and c_input == 2:
        print("Computer showed Paper \nYou won")
        u_score += 1

    else:
        print("Please enter a valid option")

    

game()

def stats():
    
    print ("Computer Score = ",c_score)
    print ("Your Score = ",u_score)


continue_input = int(input("\nDo you want to play again?\nYes = 1\nNo = 2\nStats = 3\n"))
while continue_input == 1:
        game()
        stats()
        





