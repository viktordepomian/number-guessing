import random

answer = random.randint(1, 10)
score = 5

guess = int(input("Guess a number between 1 and 10: "))

attempts = 1

while guess != answer:
    score -= 1
    if guess > answer:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")
    print("Current score:", score)
    guess = int(input("Guess a number between 1 and 10: "))
    attempts += 1

print("Correct! It took you", attempts, "attempts.")
print("Final score:", score)
