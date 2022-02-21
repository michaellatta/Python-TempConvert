#TempConvert.py
#Name: Michael Latta
#Date: 2022-02-13
#Assignment: Lab 3


def main():
    #Prompt the user for a Fahrenheit temperature
    userTempFahrenheit = input("Enter a temperature in Fahrenheit: ")

    #Convert from str to int
    userTempFahrenheit = int(userTempFahrenheit)

    #Convert that temperature to celsius, rounding to 1 decimal percision
    convertedTempCelsius = (userTempFahrenheit - 32) * 0.5556

    #Convert back from int to str for our Output
    convertedTempCelsius = str(convertedTempCelsius)

    #Output converted temperature.
    print("The Celsius temperate is " + convertedTempCelsius)

main()
