from random import randint


def main():
    lover = input('Who do you love: ')
    n = randint(0, 100)
    n = n + len(lover) % n
    print('You have a chance of ' + str(n) + '\\100  with her or him!')
    
if __name__ == "__main__":
    main()
