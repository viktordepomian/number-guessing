import random
your_points = 0


def guess_number():
    guess = int(input("Guess the number: "))


def random_number():
    number = random.randrange(1, 10)
    print(number)
    if number < guess:
        print("The number is smaller")
    elif number > guess:
        print("The number is bigger")
    elif number == guess:
        print()
    else:
        print("Correct!")




random_number()

# Gissa nummer
# Numret ska vara mellan 1-10 (import random)
# Efter 2 gissningar får man en extra hint. T.ex. Numret är mindre än 6
# Börja med 5 poäng, för varje fel försvinner 1 poäng
# EXTRA: 5 rundor, hur mycket poäng kvar efter dessa
