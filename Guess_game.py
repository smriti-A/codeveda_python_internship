import random
number = random.randint(1,100)
attempts = 5

print("Guess the number between 1 and 100")
while attempts > 0:
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("Congratulations! you guessed correctly")
        break
    elif guess > number:
        print("Too high")
    else:
        print("Too low")

    attempts = 1
    print("attempts left:", attempts)

if attempts == 0:
   print("Game Over. Number was:" , number)
