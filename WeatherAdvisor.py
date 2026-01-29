temp = int(input('Enter the temperature:'))
if temp >= 30:
    print("It's a hot day. Stay hydrated!")
elif 20 <= temp < 30:
    print("It's a warm day. Enjoy the weather!")
elif 10 <= temp < 20:
    print("It's a cool day. Wear a jacket!")
elif temp < 10:
    print("It's a very cold day. Stay warm!")