import random 

def guessing_game():
    print("""
    Welcome to Number Guessing Game!
    I have a number in mind, can you guess it? 
    You only have 6 attempts. 
    HINT: The number is between 1 - 20. 
    Good luck!
        """ )

    secret_number = random.randint(1, 20)

    for attempt in range(1,7): 
        print("Guess my secret number.")
        
        try:
            guess = int(input())
        except ValueError: 
            print("Kindly enter a number")
            return
        
        if guess > secret_number:
            print("Your guess is high, think of a lower number")
        elif guess < secret_number: 
            print("Your guess is low, the number is bigger")
        else: 
            print(f"You are right! The number is {secret_number}")
            print(f"You got it in {attempt} guesses")
            print()
            break
    else: 
        print(f"You run out of guesses! The number is {secret_number}")  
        print("Try again later")
        print()