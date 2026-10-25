#Creatte a guessing game that asks the user to find
#a secrete whole number  from 1 to 20. the program reports too low.
#too high or correct, allows at most five vali attampts,
#regect non-numeric input and regects number outside 1-20,
#invalid input ddeas not use an attempt

secret_number = 13
attempts = 0
max_attempts = 5

print("=== NUMBER GUESSING GAME ===")
print("Guess the secret number between 1 and 20.")
print("You have 5 valid attempts.")

while attempts < max_attempts:
    guess = input("Enter your guess: ").strip()

    # Reject non-numeric input
    if not guess.isdigit():
        print("Invalid input! Enter a whole number.")
        continue

    guess = int(guess)

    # Reject numbers outside the range
    if guess < 1 or guess > 20:
        print("Out of range! Enter a number from 1 to 20.")
        continue

    # Count only valid attempts
    attempts += 1

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Correct! You guessed the number.")
        print("Attempts used:", attempts)
        break

else:
    print("Game over! You used all 5 attempts.")
    print("The secret number was:", secret_number)








