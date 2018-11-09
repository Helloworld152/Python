"""
Plays a game of guess the number with the user.
"""

import random

def main():
    """
    Now the user will  give the lower limit and upper limit,
    then computer will randomly create a number which is between
    lower limit to upper limit.
    The user need guess the number.
    :return:
    """
    smaller = int(input("Enter the smaller number:"))
    larger = int(input("Enter the larger number:"))
    myNumber = random.randint(smaller, larger)
    count = 0

    while True:
        count += 1
        userNumber = int(input("Enter your guess:"))
        if userNumber < myNumber:
            print("Too small.")
        elif userNumber > myNumber:
            print("Too large.")
        else:
            print("You've got it in", count, "tries")
            break

if __name__ == '__main__':
    main()