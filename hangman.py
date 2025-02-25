import random
#print( ''')                                             
# | |                                            
# | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
# | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
# | | | | (_| | | | | (_| | | | | | | (_| | | | |
# |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
#                     __/ |                      
#                     |___/                       
# ''')
HANGMANPICS = ['''
+---+
|   |
    |
    |
    |
    |
=========''', '''
+---+
|   |
O   |
    |
    |
    |
=========''', '''
+---+
|   |
O   |
|   |
    |
    |
=========''', '''
+---+
|   |
O   |
/|  |
    |
    |
=========''', '''
+---+
|   |
O   |
/|\ |
    |
    |
=========''', '''
+---+
|   |
O   |
/|\ |
/   |
    |
=========''', 
'''
+----+
|    |
O    |
/|\  |
/ \  |
        |
=========''']

#Word bank of animals
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
        'coyote crow deer dog donkey duck eagle ferret fox frog goat '
        'goose hawk lion lizard llama mole monkey moose mouse mule newt '
        'otter owl panda parrot pigeon python rabbit ram rat raven '
        'rhino salmon seal shark sheep skunk sloth snake spider '
        'stork swan tiger toad trout turkey turtle weasel whale wolf '
        'wombat zebra ').split()

d_list = ["car"]
lives = 0

answer = random.choice(d_list)
answerList = list(answer)
print(answerList)
blanks = len(answer)

guessList =["_"] * blanks
print(guessList)
print(f"Word to guess: {"_ " * blanks}")
guessLetter = input("Guess a letter: ")

LetterList = [guessLetter]


def letterCheck(let):
        global lives
        if let not in answerList:
            lives += 1
            print(f"You guessed {guessLetter}. That's not in the word. YOU LOSE A LIFE.\n")

        for i in range(len(answerList)):
            if answerList[i] == let and guessList[i] != let:
                guessList[i] = let
    
        letterFinder(let)            
        printHangman()        


def printHangman():
    print(guessList)
    print(HANGMANPICS[lives])
    print(f"*********{6 -lives} LIVES LEFT******")

def letterFinder(let):
    if let not in LetterList:
        LetterList.append(let) 
    
    else:
        print(f"You've already guessed {let}")


while lives != 6 :
        
    letterCheck(guessLetter)
    if guessList == answerList and lives != 6:
        print("YOU WIN!!")
    else:
    
        print(guessList)
        print(f"Word to guess: {guessList}")
        guessLetter = input("Guess a letter: ")
        letterCheck(guessLetter)

                
if lives == 6:
        print(f"*********IT WAS {answerList} YOU LOSE!!!********")
    



















