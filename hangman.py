import random
print( ''')                                             
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
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
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
 

#Checking the game system with determined one word
check_word = ["cart"]
lives = 0

answer = random.choice(words)
answerList = list(answer)
print(answerList)
blanks = len(answer)

guessList =["_"]  * blanks
guessString = " ".join(guessList)
print(f"Word to guess: {guessString}")
guessLetter = input("Guess a letter: ")
checkedList = []

def letterCheck(let):
        global lives
        global checkedList

        if (let not in  answerList) and (let in checkedList):
            print(f"You've already guessed {let}") 
            lives += 1
            
        elif (let not in  answerList) and (let not in checkedList):
            
            print(f"You guessed {guessLetter}. That's not in the word. YOU LOSE A LIFE.\n")
            checkedList.append(let) 
            lives += 1

        elif let in answerList:
            for i in range (len(guessList)):
                 if answerList[i]== let:
                      guessList[i] = let

                      
        


        
              
        printHangman()        


def printHangman():
    print(guessList)
    print(HANGMANPICS[lives])
    print(f"*********{6 -lives} LIVES LEFT******")




while lives != 6 :
        
    

    if guessList == answerList:
        print("YOU WIN!!")
        break
    else:
        letterCheck(guessLetter)
        print(guessList)
        guessString = " ".join(guessList)
        if guessList == answerList:
            print("YOU WIN!!")
            break
        print(f"Word to guess: {guessString}")
        guessLetter = input("Guess a letter: ")
        

                
else:
        print(f"*********IT WAS '{answer}' YOU LOSE!!!********")
    



















