"""Wordle with six guesses!"""
____author____ = "730610651"


def contains_char(any_length: str, letter: str) -> bool:
    """Searching for letter in any_length word."""
    assert len(letter) == 1
    letter_idx: int = 0
    
    while len(any_length) > letter_idx:
        if letter == any_length[letter_idx]:
            return True
        letter_idx = letter_idx + 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Assigning color boxes with corresponding letters."""
    assert len(guess) == len(secret)
    guess_idx: int = 0
    output: str = ""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    while guess_idx < len(guess):
        if guess[guess_idx] == secret[guess_idx]:
            output = output + GREEN_BOX
        else:
            if contains_char(secret, guess[guess_idx]) is True:
                output = output + YELLOW_BOX
            else: 
                output = output + WHITE_BOX
        guess_idx = guess_idx + 1
    return output


def input_guess(num_letter: int) -> str:
    """Declare input of certain number of characters."""
    guess: str = input(f"Enter a {num_letter} character word: ")
    
    correct_num: bool = False
    while correct_num == False: 
        if len(guess) == num_letter:
            correct_num = True
        else:
          guess = input(f"That wasn't {num_letter} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    secret_num: int = len(secret_word)
    turn_num: int = 1
    win: bool = False

    while turn_num <= 6 and win is False:
        print(f"=== Turn {turn_num}/6 ===")
        guess: str = input_guess(secret_num)
        print(emojified(guess, secret_word))
        if guess == secret_word:
            win = True
        else:
            turn_num = turn_num + 1
            win = False

    if win is True:
        print(f"You won in {turn_num}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()
