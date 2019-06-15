''' Simple and wrong quote generator '''
from random import randint


def main():
    pronoms = ['I', 'you', 'he', 'she', 'they']
    verbs = ['dance', 'talk', 'walk', 'love', 'hate']
    h = ['with', 'to', 'for', '', 'on', 'over', 'under', 'in']
    subject = ['you', 'them', 'the world', 'us', 'this', 'that', 'the dog', 'the cat']
    quotes = pronoms, verbs, h, subject
    quote = ''
    for a in quotes:
        quote += ' ' + a[randint(0, len(a)-1)]
    print(quote)
if __name__ == "__main__":
    main()
