# import the random module ---------------------------
import random

# Define a list of game options: rock, paper, and scissors  ---------------------------
game_options = ["rock", "paper", "scissors"]

#Initialize player's score and rounds to zero ---------------------------
player_score = 0

#Start a while loop for the game ---------------------------
while True:
    # Prompt the player to select an option
    player_choice = input("Enter your choice (rock, paper, or scissors): ")

    # If the player enters "quit" or "q", exit the game
    if player_choice.lower() == "quit" or player_choice.lower() == "q":
        break

    # If the player enters a choice that is not in the options list, tell them to try again
    if player_choice.lower() not in game_options:
        print("Please enter a valid choice")
        continue

    # Randomly select a choice from the options list for the computer
    computer_choice = random.choice(game_options)

    # Print the computer's choice
    print(f"The computer chose {computer_choice}")

    # If the player and computer chose the same option, it's a tie
    if player_choice.lower() == computer_choice:
        print("It's a tie!")

    # If the player chose rock
    elif player_choice.lower() == "rock":
        if computer_choice == "scissors":
            print("Rock smashes scissors! You win!")
            player_score += 1
        else:
            print("Paper covers rock! You lose.")

    # If the player chose paper
    elif player_choice.lower() == "paper":
        if computer_choice == "rock":
            print("Paper covers rock! You win!")
            player_score += 1
        else:
            print("Scissors cuts paper! You lose.")

    # If the player chose scissors
    elif player_choice.lower() == "scissors":
        if computer_choice == "paper":
            print("Scissors cuts paper! You win!")
            player_score

    #Update the player's score and rounds based on the result ---------------------------
    print(f"Player score: {player_score}")

    #Ask the player if they want to continue playing ---------------------------
    play_again = input("Do you want to play again? (y/n): ")

    #If the player chooses not to continue, break the loop and end the game ---------------------------
    if play_again.lower() != "y":
        break

    #At the end of the game, print the player's score and rounds ---------------------------
    print(f"Thanks for playing! Your final score is {player_score}")