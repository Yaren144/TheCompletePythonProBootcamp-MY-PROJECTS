print('''
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa   a
8   8               8               8           8                   8   8
8   8   aaaaaaaaa   8   aaaaa   aaaa8aaaa   aaaa8   aaaaa   aaaaa   8   8
8               8       8   8           8           8   8   8       8   8
8aaaaaaaa   a   8aaaaaaa8   8aaaaaaaa   8aaaa   a   8   8   8aaaaaaa8   8
8       8   8               8           8   8   8   8   8           8   8
8   a   8aaa8aaaaaaaa   a   8   aaaaaaaa8   8aaa8   8   8aaaaaaaa   8   8
8   8               8   8   8 [^o^]   8           8          8      8   8
8   8aaaaaaaaaaaa   8aaa8   8a    8   aaaaa   8aaaaaaaa   8   aaaa8     8
8           8       8   8       8   8       8           8   8           8
8   aaaaa   8aaaa   8   8aaaa   8   8aaaaaaa8   a   a   8   8aaaaaaaaaaa8
8       8       8   8   8       8       8       8   8   8       8       8
8aaaaaaa8aaaa   8   8   8   aaaa8aaaa   8   aaaa8   8   8aaaa   8aaaa   8
8           8   8           8       8   8       8   8       8           8
8   aaaaa   8   8aaaaaaaa   8aaaa   8   8aaaa   8aaa8   aaaa8aaaaaaaa   8
8   8       8           8           8       8   8   8               8   8
8   8   aaaa8aaaa   a   8aaaa   aaaa8aaaa   8   8   8aaaaaaaaaaaa   8   8
8   8           8   8   8   8   8           8               8   8       8
8   8aaaaaaaaaaa8aaa8aaa8aaa8aaa8aaaaaaaaaaa8aaa8aaa8aaaaaaa8aaa8aaa8aaa8


''')
print("")
print("Hello player, are you lost in this maze ?")
print("**************")
print("*DONT WORRY!!*")
print("**************")
print("I can help you to get out.")
print(".")
print(".")
print(".")
choice1 = input("You\'re at the center, where do you want to go? " 
                "Type 'left' or 'right': \n\n").lower()

if choice1 == "left":

    choice2 = input("There is a greenhouse in there. "
                    "Type 'enter' for entering to the greenhouse"
                    " Type 'wait'for waiting outside: \n").lower()
    
    if choice2 == "wait":

        
        choice3 = input("You arrived at the end of the maze. There are 3 path front. "
                    "One is 'woods', one is 'golden', one is 'cotton candy'"
                    " Which one are you gonna choose? \n").lower()
        
        if choice3 == 'woods':

            print("It is the normal exit. Congratulations!!")

        elif choice3 == 'golden':

            print("You got trapped in a golden cage.You cannot escape. Game over!")

        elif choice3 == 'cotton candy':
            
            print("You enter a room full of candies and ate them all. You got sick . Game over!")
    
        else:
            
            print("You didn\'t get the game.Game over!")
    else:
        
        print("There were wasps in the greenhouse.You got stung and died!")
else:
    print("")
    print("You got lost in the maze.Game over!")




   