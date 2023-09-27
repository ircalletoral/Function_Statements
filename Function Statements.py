# Temperature Conversions
def celcious_to_fahrenheit(celsious):
    return (celsious * 9/5) + 32

def fahrenheit_to_celsious(fahrenheit):
    return (fahrenheit + 32) * (5/9)


#settign a dictionary to create selections

conversion_features = {
    "c" : celcious_to_fahrenheit ,
    "f" : fahrenheit_to_celsious
}

#Create the main engine for choice
print("Good evening! We are here to convert your desired temperature to another measuring format :) ")
print("Please select your initial measurement, so we can convert to your desired temperature")
print("C - Celsius to Fahrenheit")
print("F - Fahrenheit to Celsius")
choice = input("Enter your choice: ").strip().lower()

if choice in conversion_features:
    temperature = float(input("Please enter the initial temperature: "))

    #Conversion engine
    converted_temp = conversion_features[choice](temperature)
    converted_temp = round(converted_temp, 2)
    print(f"Your initial Temperature was {temperature} degrees {'Celsius' if choice == 'c' else 'Fahrenheit'}. This temperature is {converted_temp} degrees {'Fahrenheit' if choice == 'f' else 'Celsius'}!")

else:
    print("Try again, please input either 'C' or 'F'")
