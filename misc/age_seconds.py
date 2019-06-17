from datetime import datetime


def main():

    year  = int(input("Enter your birth year:"))
    month = int(input("Enter your month:"))
    day   = int(input("Enter your day:"))

    age = datetime.now() - datetime(year, month, day)
    print(age.total_seconds())

if __name__ == "__main__":
    main()
