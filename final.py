print("hello, this is hangman! In this game you must guess the word before the man gets hung.")
mysteryWord = "exponential"
guess1 = input("Guess a letter:")
default = ("***********")
correctLetter = ["e", "x", "p", "o", "n", "t", "i", "a", "l"]
if guess1 == "e":
        print("That is correct")
        print("e****e*****")
elif guess1 == "x":
        print("That is correct")
elif guess1 == "p":
        print("That is correct")
elif guess1 == "o":
        print("That is correct")
elif guess1 == "n":
        print("That is correct")
elif guess1 == "a":
        print("That is correct")
else: print("That is wrong")
def letter(guess, letter ):
    if guess == "e" or "x" or "p" or "o" or "n" or "t" or "i" or "a" or "l":
        print("that is correct")


    
