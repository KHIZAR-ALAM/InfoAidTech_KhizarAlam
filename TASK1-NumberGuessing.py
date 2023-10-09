import random

def number_guessing_game():

    hidden_number = random.randint(1, 100)
    
    attempts = 0
    max_attempts = 10
    
    player_name = input("Enter your name: ")
    
    print(f"Welcome, {player_name}! You have {max_attempts} attempts to guess the correct number between 1 and 100.")
    
    while attempts < max_attempts:
        try:
            
            guess = int(input("Enter your guess: "))
            
        
            if guess < hidden_number:
                print("Too low! Try again.")
            elif guess > hidden_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations, {player_name}! You guessed the secret number {hidden_number} correctly!")
                break
            
            attempts += 1
            
            print(f"Attempts remaining: {max_attempts - attempts}")
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    if attempts == max_attempts:
        print(f"Sorry, {player_name}. You've run out of attempts. The correct number was {hidden_number}.")

def replay():   
    restart = input("Do you want to play again? ").lower()
    if restart == "yes" :
       number_guessing_game()
    else:
        breakpoint   


number_guessing_game()
replay()    

