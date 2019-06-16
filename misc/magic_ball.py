from random import choice


def main():
    question = input('Ask a question: ')
    answers = ['Yes!', 'No!', 'Maybe', 'Do not count on it!', 'It\'s certain', 
            'No way!', 'Maybe']
    print(choice(answers))

if __name__ == "__main__":
    main()
