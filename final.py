import random
wordList = ["exception", "straight", "replace", "direct", "temper", "cushion", "baseline", "savant"]
word = random.choice(wordList)
wordLength = len(word)
allowedErrors = 6
done = False
guesses = []
def table():

        if allowedErrors == 6: print(""" |--------|
                                        |        
                                        |         
                                        |        
                                        |
                                        |_________""")
        try1 = """ |--------|
               |        O
               |        
               |        
               |
               |_________"""


        try2 = """ |--------|
               |        O
               |        | 
               |        
               |
               |_________"""
        try3 = """ |--------|
               |        O
               |        |\
               |        
               |
               |_________"""

        try4 = """ |--------|
               |        O
               |       /|\
               |        
               |
               |_________"""

        try5 = """ |--------|
               |        O
               |       /|\
               |         \
               |
               |_________"""

        try6 = """ |--------|
               |        O
               |       /|\
               |       / \
               |
               |_________"""
        return[table]
if wordLength == 3:
       unguessed = "_ _ _"
if wordLength == 4:
       unguessed = "_ _ _ _"
if wordLength == 5:
       unguessed = "_ _ _ _ _ _"
if wordLength == 6:
       unguessed = "_ _ _ _ _ _"
if wordLength == 7:
       unguessed = "_ _ _ _ _ _ _"
if wordLength == 8:
       unguessed = "_ _ _ _ _ _ _ _"
if wordLength == 9:
       unguessed = "_ _ _ _ _ _ _ _ _"
else:
       print("")
print(word)
while not done:
       for letter in word:
              guess = input("Guess a letter or word:")

              guesses.append(guess.lower())
              if word.lower == guesses:
                     done = True
              if guess.lower()in word.lower():
                     print("that is correct")
                     print("you have", allowedErrors, "tries remaining")
                     print(unguessed)
                     wordLength -= 1
                     if word[1] == guess:
                            unguessed[1].replace("_", guess)
                            print(guess + unguessed)
                     if word[2] == guess:
                            unguessed[3].replace("_", guess)
                     if word[3] == guess:
                            unguessed[5].replace("_", guess)
              else:
                     allowedErrors -= 1
                     print("that is incorrect")
                     print("you have", allowedErrors, "tries left")
              if allowedErrors == 0:
                     print("you have lost")
                     print("play again if you wish")
              break
if done:
       print(word, "is the correct answer!")
       allowedErrors = 6
else:
       print("That is not correct", word, "is the correct answer.")

