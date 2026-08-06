def celsius_to_fahrenheit(celsius):
    return celsius * 1.8 + 32


if __name__ == '__main__':
  celsius_t = float(input("Enter the temperature in celsius: "))
  fahrenheit_t = celsius_to_fahrenheit(celsius_t)
  print("That's {:.2f} in Fahrenheit.".format(fahrenheit_t))

  
