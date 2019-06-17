from getpass import getpass


def main():
    word = getpass('1st player choose a word:')
    print('2nd player try to guess it')
    hangword = len(word) * '_'
    print(hangword)
    while(hangword.find('_') != -1):
        guess = input('Guess a letter:')
        if guess in word:
            print(guess + ' is on it.')
            for w in range(0, len(word)):
                print(w)
                if word[w] == guess:
                    hangword = list(hangword)
                    hangword[w] = guess
                    hangword = ''.join(hangword)
            print(hangword)
        else:
            print(guess + ' isn\'t on it.')

    print('Congratz! You found the word')


if __name__ == "__main__":
    main()
