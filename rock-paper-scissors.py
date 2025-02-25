import random

rock = ('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')


paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")


scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

gameOn = 1

while gameOn:
    choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
    compChoice = random.randint(0,2)

    dict = {0: rock,1: paper, 2:scissors}

    if choice < 0 or choice >= 3:
        print("Invalid number. You lose")
        break
    print(dict.get(choice))
    print("\nComputer chose:")
    print(dict.get(compChoice))

    if choice < 0 and choice >= 3:
        print("Invalid number. You lose")

    elif choice == 0 and compChoice == 2:
            print("You win!")
            gameOn = 1
            
            
    elif choice > compChoice :
            print("You win!")
            gameOn = 1

    elif choice == compChoice:
        print("Draw")
        gameOn = 0       
    else:
        print("You lose!")
        gameOn = 0
