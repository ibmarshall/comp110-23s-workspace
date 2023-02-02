"""Ex02 - One Shot Wordle - getting closer to real thing."""
__author__ = "730610651"

secret_word: str = "python"
length_secret: int = int(len(secret_word))
guess: str = input(f"What is your {length_secret}-letter guess? ")

# with wrong amount of letters, ask to fix it
while (len(guess) != length_secret):
    guess: str = input(f"That was not {length_secret} letters! Try again: ")


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

secret_idx: int = 0
output: str = ""

# if letter is in correct position, output green box
while (secret_idx < length_secret):
    if (secret_word[secret_idx] == guess[secret_idx]):
        output = output + GREEN_BOX
    else:   
        elsewhere: bool = False
        testing_idx: int = 0

        # test for character in the rest of the word
        while (not elsewhere and testing_idx < length_secret):
            if (guess[secret_idx] == secret_word[testing_idx]):
                elsewhere = True
            else:
                testing_idx = testing_idx + 1
        # if character in wrong position, output yellow box
        if elsewhere is True:
            output = output + YELLOW_BOX
        # if character isn't in the word, output green box
        else:
            output = output + WHITE_BOX
    
    secret_idx = secret_idx + 1

print(output)

if (guess == secret_word): 
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")