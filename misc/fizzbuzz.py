def main():
    fb = 'FizzBuzz'

    for i in range(1, 1000):
        sub_fb = (fb[0+((i % 3 != 0) * 4):4+(i % 5 == 0) * 4])
        print(sub_fb) if len(sub_fb) > 0 else print(i)

if __name__ == "__main__":
    main()
