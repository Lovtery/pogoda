from operator import truediv

temperature = int(input("введите температуру "))
humidity = int(input("введите влажность "))
speed_wind = int(input("введите скорость ветра"))
is_raining = bool(input("имеются ли осадки? введите (True/False) "))

if temperature >= 25:
    print("на улице жарко!")

if temperature <= 10:
    print("на улице холодно!")

if humidity >= 80:
    print("на улице влажно!")

if speed_wind >= 10:
    print("на улице сильный ветер!!!")

if is_raining == True:
    print("возьмите зонт!!!")

if temperature >= 20 and is_raining == False:
    print("сходите в парк)")

if temperature <= 5 and speed_wind >= 8:
    print("суровая погода,оставайтесь дома!!!")

if humidity <= 30 and temperature >= 30:
    print("на улице очень сухо и жарко!!!")