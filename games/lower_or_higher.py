from random import randint


def get_user_input():
    try:
        guess = int(input("Type your guess:"))
        return guess
    except ValueError:
        print("Invalid input!", end="")
        print("Try again.")
        get_user_input()


def main():
    attempts_count = 1
    print("Try to guess a number from 1 to 1000.")
    number = randint(1, 1000)
    guess = get_user_input()
    while(guess != number):
        attempts_count += 1
        if(guess < number):
            print("Your guess is below it")
        else:
            print("Your guess is above it")
        guess = get_user_input()
    print("Congratulations, you found it! " + str(number) + ".")
    print("Number of attempts: " + str(attempts_count))

if __name__ == "__main__":
    main()