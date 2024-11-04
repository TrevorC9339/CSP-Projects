import random
wordList = ["exception", "straight", "replace", "direct", "temper", "cushion", "baseline", "savant"]
word = random.choice(wordList)

allowedErrors = 6
done = False
guesses = []

while not done:
       for letter in word:
              if letter.lower() in guesses:
                     print(letter, end=" ")
              else:
                     print("_", end=" ")
              print("")
              guess = input("Guess a letter or word:")

              guesses.append(guess.lower())

              if guess.lower() not in word.lower():
                     allowedErrors -= 1
              if allowedErrors == 0:
                     break
              done = True
              for letter in word:
                     if letter.lower() not in word:
                            done = False

if done:
       print(word, "is the correct answer!")
else:
       print("That is not correct", word, "is the correct answer.")





def table(tries):
        try0 = """ |--------|
               |        
               |         
               |        
               |
               |_________"""
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