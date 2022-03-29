import random
from statistics import median
from statistics import mode
from statistics import mean

number_attempts = []

def statistics():
    median_attempts = median(number_attempts)
    print(f"The median number of attempts is: {median_attempts}")
    mode_attempts = mode(number_attempts)
    print(f"The mode of attempts is: {mode_attempts}")
    mean_attempts = mean(number_attempts)
    print(f"The average number of attempts is: {mean_attempts}")

def start_game():
    random_number = random.randrange(1,100)
    print(random_number)
    attempts = 0
    
    while True:
        try:
            user_guess = int(input("Guess the secret number between 1 - 100: "))
            
            if user_guess > random_number:
                attempts += 1
                print("Your number is too high. Try again")
                continue
                
            elif user_guess < random_number:
                attempts += 1
                print("Your number is too low. Try again")
                continue
                
            else:
                attempts += 1
                number_attempts.append(attempts)
                print(f"You got it! It took you {attempts} attempts!")
                play_again = input("Do you want to play again? y/n ")
                if play_again.lower() == "y":
                    start_game()
                else:
                    print("Thank you for playing!")
                    statistics()        
                    
            
            break            
            
        except ValueError:
            print("Please enter a number.") 
            continue
                    
print("Welcome to the number guessing game!")
start_game()



