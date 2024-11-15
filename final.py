import random
import sys

print("Welcome! Lets play Hangman.")
def getname(name):
     name = input("what is your name", name)
getname(str)

wordList = ["time", "gap", "jump", "devolve", "weep"]
secretWord = random.choice(wordList)
print(secretWord)
guesses = ''
word = []
for i in secretWord.strip("\n"):
    word.append("_")
while wrongAttempt > 0 :
    wordStr = ''.join([str(elem) for elem in word])

    print(wordStr)
    none = 0
    letter = input("Guess a word :\t")
    for char in secretWord :
        if char == letter :
            print("Correct guess")
            word.pop(none)
            word.insert(none,char)
            none += 1
        else:
              none += 1
        if none == len(secretWord) :
                     wrongAttempt -= 1
                     print("Bad Luck. You have ",wrongAttempt," attempts left.")
                     print("The secret word is ",secretWord)
    none=0

    wordStr = ''.join([str(elem) for elem in word])
    print(wordStr)
    if wordStr == secretWord.strip("\n"):
        print("you won")
        sys.exit()
if wrongAttempt == 0 :
    print("You lost.")