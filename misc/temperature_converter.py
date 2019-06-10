

def main():
    print("1 - Celsius")
    print("2 - Fahrenheit")

    temperature_scale = int(input("Choose your temperature scale:"))
    value = float(input("Enter the value: "))

    if temperature_scale == 1:
        fahrenheit_value = value * 1.8 + 32
        print("Converting to Fahrenheit: " + str(fahrenheit_value))
    elif temperature_scale == 2:
        celsius_value = (value - 32) * 5/9
        print("Converting to Celsius: " + str(celsius_value))

if __name__ == "__main__":
    main()
