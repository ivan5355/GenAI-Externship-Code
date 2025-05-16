import random

number_to_guess = random.randint(1, 100)

user_guess = int(input("Guess a number from 1-100 "))
number_of_guess = 1

while number_to_guess!=user_guess:

    if number_to_guess==user_guess:
        number_of_guess+=1
        break
    elif user_guess<number_to_guess:
        number_of_guess+=1
        print("Too low! Try again.")
    else:
        number_of_guess+=1
        print("Too high! Try again.")

    user_guess = int(input("Guess a number from 1-100 "))

print(f"Congrats! You have guesed the number with {number_of_guess} attempts")




