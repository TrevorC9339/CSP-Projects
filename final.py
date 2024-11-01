import random
wordList = ["hello", "tall", "exceptional", "defiant", "mouse"]
def getWord():
    word = random.choice(wordList)
    return word.upper()

def play(word):
    wordCompletion = "_" * len(word)
    guessed = False
    guessedLetters = []
    guessedWords = []
    tries = 6
    print("this is hang man, you must guess teh word wihtout hanging the stickman. For every letter or words inccorect the stick man will gain a limb. Once he is complete you lose.")
    print(displayHangman(tries))
    print(wordCompletion)
    while not guessed and tries > 0:
        guess = input("guess a letter ot word").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessedLetters:
                print("already guessed this letter")
            elif guess not in word:
                print("this is not in the word")
                tires -= 1
                guessedLetters.append(guess)
            else:
                print("Correct!", guess, "Is the word!")
                multipleIndex = [i for i, letter in enumerate(word) if letter == guess]
                for index in multipleIndex:
                    wordAsList[index] = guess
                    wordCompletion = "".join(wordAsList)
                    if "_" not in wordCompletion:
                        guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            
        
    
