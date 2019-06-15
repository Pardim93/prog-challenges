from random import randint


def main():
    lenght_pw = int(input('Length of your password: '))
    pw = ''
    for x in range(0, lenght_pw):
        pw += chr(randint(33, 127))
    print(pw)
if __name__ == "__main__":
    main()