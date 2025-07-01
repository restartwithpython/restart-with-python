import random  # Import Random Library


def get_choices():  # define a function to get values from User and Computer
    player_choice = input("Enter a choice (rock, paper, scissors: ")
    options = [
        "rock",
        "paper",
        "scissors",
    ]  # Using list to store the multiple values in Single variable
    computer_choice = random.choice(
        options
    )  # Use random function to get the random values from the list
    choices = {
        "player": player_choice,
        "computer": computer_choice,
    }  # use dictionary for getting the key:variable values for player and computer and store in single variable
    return choices


def check_win(
    player, computer
):  # define a 2nd function to compare the values of both the inputs
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:  # adding condition to check who wins
        return "It's a tie!"  # return the value as string
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You lose."
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You win!"
        else:
            return "Scissors cuts paper! You lose!"
    else:
        if computer == "rock":
            return "Rock smashes scissors! You lose."
        else:
            return "Scissors cuts paper! You win!"


choices = get_choices()
result = check_win(
    choices["player"], choices["computer"]
)  # to get the value of return using keys
print(result)
