"""Plan Your Dream Vacation Game."""
___author___ = "730610651"


BEACH_EMOJI: str = "\U0001F3DD"
MONEY_EMOJI: str = "\U0001F911"
CELEBRATE_EMOJI: str = "\U0001F973"
SUNGLASSES_EMOJI: str = "\U0001F60E"

player: str = ""
points: int = 0
vacay_final: str = ""
num_vacay: int = 0


def main() -> None:
    """Run through the functions."""
    global points

    greet()
    pick_path()
    

def greet() -> None:
    """Print welcome message and ask for player's name."""
    print(f"Welcome to the Buy Your Dream Vacation Game {BEACH_EMOJI}\nYou can accumulate money {MONEY_EMOJI} in order to purchase your dream location.")
    global player
    player = input("What is our dream vacationer's name? ")


def pick_path() -> None:
    """Print path options, ask for them to choose and redirect to function."""
    global points
    next_path: bool = True
    while next_path is True:
        print(f"\n{player}, you currently have ${points} in your vacation savings account {MONEY_EMOJI}")
        print(f"\nSelect which path you would like to enter: \n1. Earn money to fund your vacation {MONEY_EMOJI}\n2. Choose your vacation location {SUNGLASSES_EMOJI}\n3. Exit the Vacation Game")
        path_num: int = int(input(f"{player} would like to proceed down path number: "))
       
        if path_num == 1:
            make_money(points)
        if path_num == 2:
            points = choose_loc(points)
        if path_num == 3:
            exit_path(points, vacay_final)
            next_path = False


def make_money(money: int) -> None:
    """Print how much money is in the savings account."""
    from random import randint
    print(f"\nYou currently have ${money} in your vacation savings account.")
   
    """Present options to make money, ask for them to choose and add points accordingly."""
    print("\nYou have four different ways of making money to add to your vacation savings account. Would you like to:\n 1. Work overtime for two weeks and receive $50\n 2. Donate plasma for $35\n 3. Downsize your home for $150\n 4. Enter the lottery for a 1/6 chance of $300")
    choice: int = int(input("Which number is your choice? "))

    if choice == 1:
        money += 50
        print(f"\nYou have selected choice number 1, to work overtime for two weeks for $50! Your new vacation savings account balance is ${money} {MONEY_EMOJI}!")
    if choice == 2:
        money += 35
        print(f"\nYou have selected choice number 2, to donate plasma for $35! Your new vacation savings account balance is ${money} {MONEY_EMOJI}!")
    if choice == 3:
        money += 150
        print(f"\nYou have selected choice number 3, to downsize your home for $150! Your new vacation savings balance is ${money} {MONEY_EMOJI}!") 
    if choice == 4:
        random_num: int = randint(1, 6)
        if random_num == 1:
            money += 300
            print(f"\nYou have selected choice number 4, to enter the lottery for a 1 in 6 chance of winning $300! You won the lotter! Your new vacation savings balance is ${money} {MONEY_EMOJI}{MONEY_EMOJI}{MONEY_EMOJI}!")
        elif random_num != 1:
            print(f"\nYou have selected choice number 4, to enter the lottery for a 1 in 6 chance of winning $300! Unforuntately, you have not won the lotter. Your vacation savings balance remains ${money}!")

    global points
    points = money


def choose_loc(money: int) -> int:
    """Print out how much money they have."""
    print(f"\n{player}, you currently have ${money}! Now you can decide how you would like to spend it! {MONEY_EMOJI}")

    """Let them know if they have the option to buy the vacation or not."""
    global vacay_final
    vacay_spot: str = input("Where is your dream vacation spot? ")
        
    from random import randint
    price: int = randint(1, 500)
    if price > money:
        print(f"\nSorry, the price to take this trip is ${price}, and you only have ${money}.")
    if price <= money:
        yes_no: str = input(f"\nThe price to travel to {vacay_spot} is ${price}. Would you like to purchase this vacation? (yes/no) ")
        global num_vacay

        """According to their answer to the previous question, provide a response."""
        if yes_no == "yes":
            money -= price
            print(f"\nYou have purchased a vacation to {vacay_spot} for ${price} {CELEBRATE_EMOJI} You now have ${money} in your vacation savings account!")
            if num_vacay == 0:
                vacay_final = (f"{vacay_spot}")
            elif num_vacay > 0:
                vacay_final = (f"{vacay_final} and {vacay_spot}")
            num_vacay += 1
        elif yes_no == "no":
            print(f"\nYou have rejected the trip to {vacay_spot} for ${price}.")
    return money


def exit_path(points: int, vacay_final: str) -> None:
    """Print out how much money they have and the vacations they planned."""
    if num_vacay == 0:
        print(f"\n{player}, you did not successfully plan a trip, but you have ended with ${points} in your vacation savings account!")
    else:
        print(f"\n{player}, you have ended with a vacation to {vacay_final} and ${points} in you vacation savings account!")
        print("Plan a trip again with us soon!")


if __name__ == "__main__":
    main()