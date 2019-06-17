def main():

    integer = input('Enter your interger: ')

    while integer != 1:
        if integer % 2 == 0:
            integer /= 2
            print(integer)
        else:
            integer = integer * 3 + 1
            print(integer)

if __name__ == "__main__":
    main()
