import random

life_points = 5
number_to_guess = random.randint(1, 100)
# print(number_to_guess)
print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100.")
print(f"You have {life_points} attempts to guess the number.")
    
while life_points > 0:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
        
    if guess < 1 or guess > 100:
        print("Please guess a number between 1 and 100.")
        continue
    
    if guess == number_to_guess:
        print(f"Congratulations! You guessed the number correctly. It was {number_to_guess}.")
        break
    elif guess < number_to_guess:
        print("Too low!")
    else:
        print("Too high!")
        
    life_points -= 1
    print(f"You have {life_points} attempts left.")
        
    if life_points == 0:
        print(f"Game Over! You've run out of attempts. The number was {number_to_guess}.")
