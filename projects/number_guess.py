import random

user_number = input("Type a number: ")

if user_number.isdigit():
    user_number = int(user_number)

    if user_number <= 0:
        print("Please Provide a positive digit")
        quit()
else:
    print("Please provide a number")
    quit()

random_number = random.randint(0, user_number)
number_of_guesses = 0

while True:
    number_of_guesses += 1
    user_guess = input("Make a number guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a valid digit")
        continue

    if user_guess == random_number:
        print("Congrats you got it right!")
        break
    elif user_guess > random_number:
        print("Your guess is above the number")
    else:
        print("Your guess is below the number")

print(f"You got it after {number_of_guesses}  guesses")