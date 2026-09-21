import random 
print("""
Welcome to Number Guessing Game!
I have a number in mind, can you guess it? 
You only have 6 attempts. 
HINT: The number is between 1 - 20. 
Goodluck!!!
     """ )

secret_number = random.randint(1, 20)

for num in range(6): 


if guess == secret_number:
    print("")
else: 
    print("")