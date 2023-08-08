def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

print("Temperature Conversion:")
print("1. Fahrenheit to Celsius")
print("2. Celsius to Fahrenheit")
print("3. Exit")
while True:
    choice = int(input("Enter your choice (1, 2, 3): "))

    if choice == 1:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit:.2f} Fahrenheit is equal to {celsius:.2f} Celsius.")
    elif choice == 2:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius:.2f} Celsius is equal to {fahrenheit:.2f} Fahrenheit.")
    elif choice ==3:
        print("Exiting Temperature Converter")
        break
    else:
        print("Invalid choice. Please choose 1, 2, 3.")