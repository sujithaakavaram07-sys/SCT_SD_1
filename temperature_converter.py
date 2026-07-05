print("=====Temperature Converter=====")
print("Choose the unit of the temperature.")
print("1.Celsius")
print("2.Fahrenheit")
print("1.Kelvin")
choice=int(input("Enter your choice(1-3):"))
temperature=float(input("Enter the temperature"))
if choice==1:
    fahrenheit=(temperature*9/5)+32
    kelvin=temperature+273.15

    print("\nConverted Temperatures.")
    print("Celsius:",temperature,"°C")
    print("Fahrenheit:",round(fahrenheit,2),"°F")
    print("Kelvin:",round(kelvin,2),"K")
elif choice==2:
    celsius=(temperature-32)*5/9
    kelvin=celsius + 273.15
    print("\nConverted Temperatures:")
    print("Fahrenheit:", temperature, "°F")
    print("Celsius:", round(celsius, 2), "°C")
    print("Kelvin:", round(kelvin, 2), "K")

elif choice==3:
    celsius=temperature-273.15
    fahrenheit=(celsius*9/5)+32
    print("\nConverted Temperatures:")
    print("Kelvin:", temperature, "K")
    print("Celsius:", round(celsius, 2), "°C")
    print("Fahrenheit:", round(fahrenheit, 2), "°F")
else:
    print("Invalid choice! Please run the program again.")
    
