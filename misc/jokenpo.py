from random import randint


def main():
    jkp = ['Scissors', 'Paper', 'Rock']
    user_score = cpu_score = 0
    print('Jokenpo! Best of 3:')

    while((user_score < 3) and (cpu_score < 3)):
        choice = int(input('1 - Scissors\n2 - Paper\n3 - Rock\n'))
        cpu_choice = randint(1, 3)        
        print('You chose: ' + jkp[choice - 1])
        print('CPU chose: ' + jkp[cpu_choice - 1])

        if choice % 3 + 1 == cpu_choice:
            user_score += 1
            print('You won!')
        elif cpu_choice % 3 + 1 == choice:
            cpu_score += 1
            print('CPU won!')
        else:
            print('Draw!')
        
if __name__ == "__main__":
    main()
